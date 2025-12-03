
# Linked Lists

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1400%2F0*0XVK02Guco9xJMJL.png&f=1&nofb=1&ipt=0ebff9ae76fd9ac20c62349634ff5ef08a26c279a68a889b73abd96ac3bcde28)

Linked lists are ideal for anything that requires modification to the beginning (or end for doubly linked lists)


## Singly Linked Lists

- There is a `Head` node 
- Nodes have a `next` pointer


## Doubly Linked Lists

- There is a `Head` and `Tail` node
- Nodes have a `next` and `prev` pointer


## Operations

1. Traversal
2. Modify (insert/delete/update) at beginning
3. Modify at end
4. Modify at position `i`
5. Peek head
6. Peek tail
7. Lookup a value


## Time Complexity

|                     | Singly LL | Doubly LL | 
|:--------------------|:----------|:----------|
| Traversal           | O(n)      | O(n)      |
| Modify beginning    | O(1)      | O(1)      |
| Modify end          | O(n)      | O(1)      |
| Modify position `i` | O(n)      | O(n)      |
| Peek at head        | O(1)      | O(1)      |
| Peek at tail        | O(n)      | O(1)      |
| Lookup a value      | O(n)      | O(n)      |
