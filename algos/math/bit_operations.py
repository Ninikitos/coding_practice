# Left shift points at it. XOR flips the bit.
def toggle_bit(n, p):
    return n ^ (1 << p)

print(toggle_bit(5, 1))

# OR forces a bit to 1.
def set_bit(n, p):
    return n | (p << 1)

print(set_bit(5, 1))

# AND with a flipped mask forces it to 0.
def clear_bit(n, p):
    return n & ~(1 << p)

print(clear_bit(5, 1))

# Shift the target bit to position 0, then read it.
def is_bit_set(n, p):
    return (n >> p) & 1 == 1

# Same operators — but now the mask is already built.
def set_multiple_bits(n, mask):
    return n | mask

def clear_multiple_bits(n, mask):
    return n & ~mask

print(clear_multiple_bits(5, 1))

def toggle_multiple_bits(n, mask):
    return n ^ mask

print(toggle_multiple_bits(5, 3))