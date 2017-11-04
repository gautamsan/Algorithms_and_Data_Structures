"""1. Count Bits"""


# Runtime: O(n) => n = number of bits needed to represent integer, 8 here
def count_bits(x):
    num_bits = 0
    while x > 0:
        num_bits += x & 1  # 1 is added only when x is 1 because 1 & 1 == 1
        x = x >> 1  # drop rightmost bit one by one
    return num_bits


# print(count_bits(int('10010111', 2)))


"""2. Parity"""


# if parity is 1, odd number of ones, eg.0111
# if parity is 0, even number of ones eg.0101
# Runtime: O(n) => n = number of bits needed to represent integer, 8 here
def parity(x):
    result = 0
    while x:
        # XOR between two nums a and b is same as (a+b) mod 2
        # Our only concern is even or odd number of bits
        result ^= x & 1  # x & 1 == 1 only if x = 1
        x >>= 1

    return result


# print(parity(int('10010111', 2)))


"""3. Parity improvement: Erasing lowest set bit in one operation"""


# Trick: x & (x-1) Erases lowest set bit
# Runtime: O(k) => k = number of set bits i.e 1 bits
# Improves best and average cases because in worst case all bits are set
def parity1(x):
    result = 0
    while x:
        print(bin(x))
        # XOR with 1 because every loop erases lowest set bit
        # i.e, 1 is encountered on every loop
        result ^= 1  # 0 ^ 0 == 0, 1 ^ 1 == 0, else 1
        x &= x-1  # Drops lowest set bit
    return result

print(parity1(int('00010111', 2)))

