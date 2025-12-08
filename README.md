
personal notes + code examples

best [youtube playlist](https://www.youtube.com/playlist?list=PLKYEe2WisBTGq9T0wPulXz1otUsVeOGey) to review/refresh on DSA


## Index

### Data Structures
[`binary trees`](./data_structures/binary_trees/README.md)<br>
[`graphs`](./data_structures/graphs/README-old.md)<br>
[`hash sets & maps`](data_structures/hash_tables/README.md)<br>
[`heaps`](./data_structures/heaps/README.md)<br>
[`linked lists`](./data_structures/linked_lists/README.md)<br>
[`queues`](./data_structures/queues/README.md)<br>
[`stacks`](./data_structures/stacks/README.md)<br>

### Algorithms
[`dynamic programming`](./algorithms/dynamic_programming/README.md)<br>
[`recursion`](./algorithms/recursion/README.md)<br>
[`search_algorithms`](./algorithms/search_algorithms)<br>
[`sorting algorithms`](./algorithms/sorting_algorithms)<br>

### Other
[`binary and bit manipulation`](./binary_bit_manipulation/README.md)<br>

## Leetcode Solution Approach Guide

- *kth largest/smallest* -> heap
- *substring* -> two pointer or sliding window
- *exhaustive/brute-force search* -> recursive backtracking


## Time & Space Complexity

**Time Complexity**: measures how # of OPERATIONS needed increases with INPUT SIZE
- Best, average, and worst case scenarios are considered 
  - Ex: for a sorting problem, best case is input is already sorted, worst case is it's sorted in opposite order, average is somewhere in between

**Space Complexity**: measures how MEMORY SPACE needed increases with INPUT SIZE
- This does not reflect the size of the _provided_ input. It measures how much ADDITIONAL space your algorithm demands 
to perform operations on the input. 

**Big-O Notation**: worst case complexity
- Constants are ignored because they become trivial as the input grows very large
  - Ex: Doing five loops through an array is 5n -> reduces to O(n)
- Smaller polynomials are disregarded, because the worst polynomial drives the complexity
  - Ex: O(3n^2 + 2n + logn) -> O(n^2)

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1400%2F1*5ZLci3SuR0zM_QlZOADv8Q.jpeg&f=1&nofb=1&ipt=b5e50d4d9b07c8caeff2bc98c94bf745e942664241590b43e5b8b91a9c2defbb)

**O(1)**:
- Time: An immediate lookup
- Space: Using a fixed number of variables regardless of input size

**O(n)**:
- Time: Iterating through each item `n` in the data structure
- Space: Storing the `n` items in a new data structure

**O(n^2)**:
- Time: A nested loop where for each element `n` in the input, you loop through all other elements in the input
- Space: Storing a data structure of size `n * n`

**O(logn)**:
- Halving the operations needed at each iteration

**O(n logn)**: 
- A logarithmic operation is performed for each element `n` in the input

**O(2^n)**:
- Doubling the operations needed at each iteration

**O(n!)**:
- Typically a brute force solution, like considering all
possible permutations of an input
