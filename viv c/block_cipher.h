#pragma once

typedef unsigned char byte;

// The block size
#define BLOCK_SIZE_BITS  128
#define BLOCK_SIZE_BYTES BLOCK_SIZE_BITS/8
#define ROUNDS 10

// Declaration of public methods

// Receives a block and a key
void enc_block(byte* block, const byte* key);

// Receives a block and a key
void dec_block(byte* block, const byte* key);