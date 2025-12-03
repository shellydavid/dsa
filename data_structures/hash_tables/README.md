
# Hash Sets & Maps

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.sahinarslan.tech%2Fstatic%2F34a1965ce85b83bbf3ae793be9fae6ec%2Fa2510%2Fhash-table-wikipedia.jpg&f=1&nofb=1&ipt=db0eff670c92ab33eb94405d57244a7e0deb53d2c439b56a58c13ceef189f741)


## Hash Function

Takes a value and hashes it to return an index

### Collisions
**Collision**: multiple values hashing to the same index

- **Separate chaining**: store collisions as a linked list in the same bucket
- **Linear probing**: check sequentially for the next avail bucket
- **Quadratic probing**: use a quadratic function to find the next avail bucket

### What is Hashable
Only immutable data types can be hashed
- **Python immutable types**: strings, integers, floats, tuples
- **Python mutable types**: lists, dicts


## Hash Sets

A hashed collection of _unique_ elements

> The Python `set()` function is a hash set


## Hash Maps

A `key:value` pair mapping

Keys must be hashable

> The Python `dict {}` data type is a hash map


## Time Complexity

|        | Hash Set | Hash Map | 
|:-------|:---------|:---------|
| Lookup | *O(1)    | *O(1)    |
| Add    | O(1)     | O(1)     |
| Delete | O(1)     | O(1)     |

Lookups are amortized `*O(1)`, bec bad collisions are possible `O(n)` but _very_ unlikely with a good hash function