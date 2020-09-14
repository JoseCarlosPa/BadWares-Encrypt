#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "block_cipher.h"

// 10 MB max file size 
#define MAX_FILE_SIZE 100000000

void print_bytes(byte* data, const byte* key, const int n) {
	// Print n bytes
	int i;
	for (i = 0; i < n; i++) printf("%02x", data[i]);
	// Enter
	putchar('\n');
}

// Function to decode a key from the command line into a 128 bit location in memory
// Source: https://stackoverflow.com/a/35452093
byte* datahex(char* string) {

    if (string == NULL)
        return NULL;

    size_t slength = strlen(string);
    if ((slength % 2) != 0) // must be even
        return NULL;

    size_t dlength = slength / 2;

    byte* data = malloc(dlength);
    memset(data, 0, dlength);

    size_t index = 0;
    while (index < slength) {
        char c = string[index];
        int value = 0;
        if (c >= '0' && c <= '9')
            value = (c - '0');
        else if (c >= 'A' && c <= 'F')
            value = (10 + (c - 'A'));
        else if (c >= 'a' && c <= 'f')
            value = (10 + (c - 'a'));
        else {
            free(data);
            return NULL;
        }

        data[(index / 2)] += value << (((index + 1) % 2) * 4);

        index++;
    }

    return data;
}

void encrypt(byte* data, const size_t len, const byte* key) {
    const size_t blocks = len / 16 + (len % BLOCK_SIZE_BYTES != 0);
    size_t i;
    for (i = 0; i < blocks; i++) {
        byte* current_block = data + (i * BLOCK_SIZE_BYTES);
        enc_block(current_block, key);
    }
}

void decrypt(byte* data, const size_t len, const byte* key) {
    const size_t blocks = len / 16 + (len % BLOCK_SIZE_BYTES != 0);
    size_t i;
    for (i = 0; i < blocks; i++) {
        byte* current_block = data + (i * BLOCK_SIZE_BYTES);
        dec_block(current_block, key);
    }
}

int main(int argc, char* argv[]){
    if (argc != 5) {
        printf("Usage: %s [e/d] key in_file out_file\n", argv[0]);
        return -1;
    }

    // Try to open in and out
    const char* in_file  = argv[3];
    const char* out_file = argv[4];

    FILE* in  = fopen(in_file,  "rb");
    FILE* out = fopen(out_file, "wb");

    if (in == NULL || out == NULL) {
        puts("Ocurrio un error al abrir los archivos");
        return -2;
    }

    // Good files, decode key from command line
    const byte* key = datahex(argv[2]);

    // Key in memory, read input file in memory
    byte* data = malloc(MAX_FILE_SIZE);
    memset(data, 0, MAX_FILE_SIZE);
    fseek(in, 0, SEEK_END);
    size_t fsize = ftell(in);
    fseek(in, 0, SEEK_SET);  /* same as rewind(f); */
    fread(data, sizeof(byte) , fsize, in);
    fclose(in);

    const char mode = argv[1][0];
    if (mode == 'e') {
        puts("Encrypting...");
        encrypt(data, fsize, key);
        // Data encrypted, write to out file
        size_t blocks = fsize / 16;
        if (fsize % 16 != 0) blocks++;
        fsize = blocks * 16;
        fwrite(data, sizeof(byte), fsize, out);
        fclose(out);
        decrypt(data, fsize, key);
    }
    else if (mode == 'd') {
        puts("Dec");
        decrypt(data, fsize, key);
        fwrite(data, sizeof(byte), fsize, out);
    }


	return 0;
}
