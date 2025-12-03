"""
Binary Conversions
"""

# -------- Decimal to Binary --------
# Use built in bin function
print(bin(5))

# It will be prefixed by '0b' to indicate the base, so you can index this out
print(bin(5)[2:])


# -------- Hex --------
# Use built-in hex function
hex(5)


# -------- Binary to Decimal --------
# Use built-in `int` function, passing the base of the number as second argument
binary_5 = '101'
print(int(binary_5, 2))
