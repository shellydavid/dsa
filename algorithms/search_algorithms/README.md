# Search Algorithms

## Binary Search - `O(log n)`

Given a target value and a *sorted* array, find the middle value `M`.

- If the target value is < `M`, you can eliminate the entire right half of the search space
- If the target value is > `M`, you can eliminate the entire left half of the search space

Repeat until target is found or search space is exhausted (no match)

<img src='../../img/binary-search.webp'>