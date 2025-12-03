"""
Queues (FIFO)

----- Operations -----
1. is_empty
2. enqueue
3. dequeue

----- Implementation -----
Because they are First in First out,
queues ADD to the R and DEQUEUE from the L

> Dynamic arrays are NOT suitable here, because deleting
the first element destroys the reference to the array
and will ALWAYS require resizing O(n)

> Doubly linked lists are better, because modifying
the head or tail is always O(1)
"""


# Utilizing the built-in `deque` object (double ended queue)
# It's a doubly linked list - can push/pop from L in O(1) and push/pop from R in O(1)
# Can be used then as a stack or queue
# They can be indexed like a list
from collections import deque


class Queue:
	def __init__(self):
		self.q = deque()

	def is_empty(self):
		return len(self.q) == 0

	def enqueue(self, val):
		# Queues append from R
		self.q.append(val)

	def dequeue(self):
		# Queues pop from L
		return self.q.popleft()

	def peek(self):
		return self.q[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.q)

q.dequeue()
print(q.q)
q.dequeue()
print(q.q)
q.dequeue()
print(q.q)
