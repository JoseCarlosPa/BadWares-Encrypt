#include "block_cipher.h"
#include <string.h>

void dec_round(byte* block, const byte* key) {
	// Reverse the massive XOR
	int i;
	for (i = 0; i < 16; i++) block[i] ^= key[i];

	//reverse the permutation
	byte c[BLOCK_SIZE_BYTES];
	memcpy(c, block, BLOCK_SIZE_BYTES);

	// Refer to the permutation matrix
	block[0]  = c[13];
	block[1]  = c[10];
	block[2]  = c[7];
	block[3]  = c[0];
	block[4]  = c[14];
	block[5]  = c[11];
	block[6]  = c[4];
	block[7]  = c[1];
	block[8]  = c[15];
	block[9]  = c[8];
	block[10] = c[5];
	block[11] = c[2];
	block[12] = c[12];
	block[13] = c[9];
	block[14] = c[6];
	block[15] = c[3];
}

void dec_block(byte* block, const byte* key) {
	// 10 rounds of dec
	int i;
	for (i = 0; i < ROUNDS; i++)
		dec_round(block, key);
}