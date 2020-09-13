#include "block_cipher.h"
#include <string.h>

void enc_round(byte* block, const byte* key) {
	// Copy the block to a temporary section
	byte old_block[BLOCK_SIZE_BYTES];
	memcpy(old_block, block, BLOCK_SIZE_BYTES);

	// Perform permutation using the permutation matrix
	block[0]  = old_block[3];
	block[1]  = old_block[7];
	block[2]  = old_block[11];
	block[3]  = old_block[15];
	block[4]  = old_block[6];
	block[5]  = old_block[10];
	block[6]  = old_block[14];
	block[7]  = old_block[2];
	block[8]  = old_block[9];
	block[9]  = old_block[13];
	block[10] = old_block[1];
	block[11] = old_block[5];
	block[12] = old_block[12];
	block[13] = old_block[0];
	block[14] = old_block[4];
	block[15] = old_block[8];

	// Massive XOR with the key
	int i;
	for (i = 0; i < 16; i++) block[i] ^= key[i];
}

void enc_block(byte* block, const byte* key) {
	int i;
	// Make 10 rounds of this block
	for (i = 0; i < ROUNDS; i++) enc_round(block, key);
}