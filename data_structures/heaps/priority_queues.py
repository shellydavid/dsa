"""
Priority Queues
------------------------------

Priority queues are min heaps

The trick is to put tuples in your heap.
First value is the priority. Second is the data or object itself.

This way, you can effectively store and retrieve data by priority
via a single data structure
"""


import heapq

A = [(3, 'Sarah'), (2, 'Jim'), (1, 'Bob'), (4, 'Alice')]

print('Original array: ', A)

heapq.heapify(A)
print('\nMin heapified array: ', A)

print('\nHeap pop')
for i in range(len(A)):
	next = heapq.heappop(A)
	print(f"{next[0]}: {next[1]}")
print(A)
