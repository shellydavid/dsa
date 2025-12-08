# Dynamic programming
Aims to optimize problems that have overlapping sub-problems

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20240319104901%2Fdynamic-programming.webp&f=1&nofb=1&ipt=693160f48d98e92eb729843264370a5900a9775aa2824048670c34afa8356d12)


## Levels/Steps
1. Naive recursive solution
2. Top-Down (memoization)
3. Bottom-Up (tabulation)
4. Bottom-Up with constant space


## Naive Recursive Solution
First, consider the naive recursive solution without dynamic programming at all

This will typically have a very large runtime (2<sup>n</sup> or n!) due to overlapping sub-problems


## Top-Down (Memoization) - RECURSION
Recursion, but with a cache for storing solutions to already-seen problems

Use a hashmap/set to store base case values, then store values of other sub-problems as you go


## Bottom-Up (Tabulation) - ITERATIVE
Iterate and store solutions in a table (array, etc)

Some problems can be further optimized to use a constant-space solution

**Bottom-Up is generally preferred to Top-Down because**: 
- Programming languages are better suited for loops than recursion
- It can sometimes be optimized to have a constant-space solution (whereas recursion always uses a call stack)