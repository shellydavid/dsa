
# Queues

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.LFNjMGnC1PgZKUxkLQ6i0gHaDt%3Fpid%3DApi&f=1&ipt=0cd35e7dae9b00ea32c41e8ed44cedeea05128235e5ff7098d9f252373508686&ipo=images)

**FIFO**: First In, First Out


## Representations

- Array - _INEFFICIENT_: 
  - Items are added (enqueued) to the right and removed (dequeued) from the left
  - Removing from the left of an array (i.e. first index) is inefficient because you will always have to shift the elements
- Linked List - _IDEAL_: 
  - The head is modified to dequeue and the tail is modified to enqueue (both constant time operations)
 

## Operations

1. Enqueue
2. Dequeue
3. isEmpty


## Time Complexity

|         | Dynamic Array | Linked List | 
|:--------|:--------------|:------------|
| Enqueue | *O(1)         | O(1)        |
| Dequeue | O(n)          | O(1)        |
| isEmpty | O(1)          | O(1)        |
