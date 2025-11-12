# Makefile for avx_subset_mem test
# Separate flags for ASM and C so the harness does NOT accidentally emit AVX scalars.

CC := gcc
CFLAGS := -O2 -std=c11 -Wall -Wextra -mno-avx -msse2
ASFLAGS := -O2 -mavx
LDFLAGS := -static

SRC_ASM := avx_subset_mem.S
SRC_C   := harness_mem.c
OBJ := $(SRC_ASM:.S=.o) $(SRC_C:.c=.o)
BIN := avx_subset_mem_test

all: $(BIN)

%.o: %.S
	$(CC) $(ASFLAGS) -c $< -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(BIN): $(OBJ)
	$(CC) $(OBJ) -o $@ $(ASFLAGS) $(LDFLAGS)

clean:
	rm -f $(OBJ) $(BIN)

.PHONY: all clean
