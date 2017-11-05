"""
Important Bit Concepts:
1. Create a mask at position
    - First take bit 1 ie. 00000001.
    - Then, left shift by desired Position. eg (1 << 2) = 00000100
    - Mask is created at position 2.
    ** Masks can be used to set, clear toggle and get bits at different positions **

2. Set bit at position (Make it 1):
    - given_number | Mask

3. Toggle bit at position:
    - given_number ^ Mask

4. Clear bit at position (Make it 0):
    - given_number & ~(Mask)
    ** If Mask = 00000100 then ~(Mask) = 11111011 **

"""

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

# print(parity1(int('00010111', 2)))


"""4. Parity improvement: Parity with cache"""

# To compute parity of 64 bit words, we store parities of four 16-bit sub-words
# Parity of whole word is found by computing parity of four sub-words

# -------- Example for 2-bit words -----------
precomputed_parity_2bit = [parity(i) for i in range(1 << 2)]

# lookup table for 2-bit words
print(precomputed_parity_2bit)  # [0, 1, 1, 0] => Parities of (0,0), (0,1), (1,0) and (1,1)
print(len(precomputed_parity_2bit))  # 4 entries

# To compute parity of 11001010 ie. sub-words: (11)(00)(10)(10),
# We look in the table to find parity of (11) == 0, parity of (00) == 0, parity of (10) == 1, parity of (10) == 1
# Parity of whole word is parity of 0,0,1,1 == 0

# -------- End example for 2-bit words -----------

# ************************ 64-bit word *****************************************
precomputed_parity = [parity(i) for i in range(1 << 16)]
print(len(precomputed_parity))  # 65,536 entries
# print(bin(0xFFFF))


def parity_cached(x):
    mask_size = 16
    # mask has 16 1's because we need to extract 16 bits at a time to use as index into the lookup table
    bit_mask = int('0b1111111111111111', 2)
    return (
        # right-shift 48 bits to find parity of first 16 bits '1111111100001000'
        precomputed_parity[x >> (3 * mask_size)] ^
        # need to '&' because we are shifting only 32 bits and previously
        # calculated 16-bits are still there. '&' sets those bits to 0
        precomputed_parity[x >> (2 * mask_size) & bit_mask] ^
        precomputed_parity[x >> mask_size & bit_mask] ^
        precomputed_parity[x & bit_mask]
        )

# Finding index
#
# 1111111100001000 1111111100000100 1111111100000010 1111111100000001
# - 1st operation:
#   11111111100001000 => Rshift 48 gives Index for lookup table.
#
# - 2nd operation:
#   #  1111111100001000 # 1111111100000100 => Rshift 32 [# dddd # means not needed]
#   &  0000000000000000   1111111111111111
#  ------------------------------------------
#      0000000000000000   1111111100000100 => Index for lookup table. Not needed bits are erased

# - 3rd operation:
#   #  1111111100001000 1111111100000100 # 1111111100000010 => Rshift 16 [# dddd # means not needed]
#   &  0000000000000000 0000000000000000   1111111111111111
#  -----------------------------------------------------------
#      0000000000000000 0000000000000000   1111111100000010 => Index for lookup table. Not needed bits are erased
#
# - 4th operation: Take whole thing
#   #  1111111100001000 1111111100000100 1111111100000010 # 1111111100000001 [# dddd # means not needed]
#   &  0000000000000000 0000000000000000 0000000000000000   1111111111111111
#  ------------------------------------------------------------------------------------
#      0000000000000000 0000000000000000 0000000000000000   1111111100000001 => Index. Not needed bits are erased
#

#

print(parity_cached(int('0b1111111100001000111111110000010011111111000000101111111100000001', 2)))


