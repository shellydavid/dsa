# Search Algorithms

## Binary Search - `O(log n)`

Given a target value and a *sorted* array, find the middle value `M`.

- If the target value is < `M`, you can eliminate the entire right half of the search space
- If the target value is > `M`, you can eliminate the entire left half of the search space

Repeat until target is found or search space is exhausted (no match)

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20240506155201%2Fbinnary-search-.webp&f=1&nofb=1&ipt=1378985fe16aef7f45d48ff5800d8bb30b3e8c35ec7105aba0e55dbc6595218f)