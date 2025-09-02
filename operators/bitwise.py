# Bitwise Operators:
# Used to perform operations at the binary (bit) level on integers. 
# & (Bitwise AND)
# | (Bitwise OR)
# ^ (Bitwise XOR)
# ~ (Bitwise NOT)
# << (Left shift)
# >> (Right shift)

# 2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
# 128 64  32  16  8   4   2   1

# 32
# 16
# 57 - 48 = 9

# 3 - Decimal
# 0011 - Binary

# 5 - Decimal
# 0101 - Binary

# 17 - Decimal
# 10001 - Bianry

# 57 - Decimal
# 111001 - Binary
# a = 3
# b = 5

# 0- False
# 1- True

# A B & | ^ ~
# 0 0 0 0 0 1
# 0 1 0 1 1 1
# 1 0 0 1 1 0
# 1 1 1 1 0 0


a = 3
b = 5
# 0001 - Decimal (1)
# print(a & b)

# 0111 - Decimal (7)
# print(a | b)

# 0110 - Decimal (6)
# print(a ^ b)


# << (Left shift)
# >> (Right shift)

# 7 - 00000111 - 128bit

a = 7
a = a<<3
print(a)

# 00000111
# 00111000 - Decimal (56)

# a = 97
# A = 65