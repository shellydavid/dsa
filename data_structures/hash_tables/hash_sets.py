"""
Hash Sets
"""

s = set()

# Add items
# Adding a mutable type will raise a TypeError
s.add(1)
s.add("hello")
s.add((3, 4, 5))
s.add(1.23)
print('Hash set: ', s)


# Lookup
print('\nLookup items in set')
print(1 in s)
print("hello" in s)


# Remove
print('\nRemove items from set')
s.remove(1)
print(s)


# Make a set from a string (Set construction)
print('\nSet construction')
foo = "aaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccddddddddddd"
unique_chars = set(foo)
print(unique_chars)
