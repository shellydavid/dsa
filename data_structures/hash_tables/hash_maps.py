"""
Hash Maps
"""


# -------- Basic dict/hashmap --------
d = {"a": 1, "b": 2}


# Add key:val
d["c"] = 3
print('Hash map: ', d)


# Lookup if key exists
print("c" in d)
print("z" in d)


# Lookup a key's value
# If key does not exist, the below syntax will raise a KeyError
print(d["c"])
print(d["b"])


# Display all keys
print(d.keys())


# Display all values
print(d.values())


# Display all key:value pairs
print(d.items())


# Loop through key:value pairs
for key, val in d.items():
	print(key, val)



# -------- defaultdict --------
from collections import defaultdict

# Create a dictionary where items have a default int value (0)
default = defaultdict(int)
# default = defaultdict(list)  will be empty list [], etc...

# Indexing non-existent keys will return the default value instead of KeyError
print(default[2])



# -------- Counter --------
from collections import Counter

# Create a hashmap that counts the frequency of unique elements in an input
string = "aaaaaabbbccccddddeeeeeeeeeeeefffg"
unique_counts = Counter(string)
print(unique_counts)

# This can easily be done from scratch too
unique_counts = {}
for c in string:
	if c not in unique_counts:
		unique_counts[c] = 1
	else:
		unique_counts[c] += 1
print(unique_counts)

# And with defaultdict
unique_counts = defaultdict(int)
for c in string:
	unique_counts[c] += 1
print(unique_counts)
