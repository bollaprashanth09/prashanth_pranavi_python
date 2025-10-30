# Implementation of Bitwise Operators in Python 

# Create two variables
a = 60   # 60 = 0b111100
b = 13   # 13 = 0b1101

# Bitwise AND, OR, XOR
print("Bitwise AND: 60 & 13 =", a & b, "(binary:", bin(a & b) + ")")
print("Bitwise OR: 60 | 13 =", a | b, "(binary:", bin(a | b) + ")")
print("Bitwise XOR: 60 ^ 13 =", a ^ b, "(binary:", bin(a ^ b) + ")")
# Bitwise NOT
print("Bitwise NOT: ~60 =", ~a, "(binary:", bin(~a) + ")")

# Bitwise Shifts
print("Bitwise Left Shift: 60 << 2 =", a << 2, "(binary:", bin(a << 2) + ")")
print("Bitwise Right Shift: 60 >> 2 =", a >> 2, "(binary:", bin(a >> 2) + ")")
