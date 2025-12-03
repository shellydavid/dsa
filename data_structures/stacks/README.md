
# Stacks

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.YhoVsNJLcYskqnaxdccE6gHaGO%3Fpid%3DApi&f=1&ipt=93b81dfd34f32e9d7e338f36a07c37556a82d624daa8c92bd64bb3a28a34f0a2&ipo=images)

**LIFO**: Last In, First Out


## Representations

- Array - _GOOD_: 
  - Items are pushed/popped from the right end of the array
  - Appending to a dynamic array can *sometimes* require resizing
- Linked List - _MOST EFFICIENT_: 
  - The tail is modified to push/pop
  - In (doubly) linked lists, adding to the end is *always* constant


## Operations

1. **Push**
2. **Pop**
3. **Peek**
4. **isEmpty**


## Time Complexity

|               | Dynamic Array | Linked List | 
|:--------------|:--------------|:------------|
| Push (append) | `*O(1)`         | `O(1)`       |
| Pop           | `O(1)`          | `O(1)`        |
| Peek          | `O(1)`          | `O(1)`       |
| isEmpty       | `O(1)`          | `O(1)`        |
