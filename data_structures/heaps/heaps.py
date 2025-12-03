"""
Heaps

Operations:
- Heapify: O(n)
- Heap pop (extract min/max): O(log n) (popping the top is constant time, but fixing the tree is log n)
- Heap push (insert): O(log n)
- Heap peek: O(1)
- Heap sort: O(n * log n)

Heaps can be represented as arrays. This is efficient only of the tree is relatively balanced.
Otherwise, linked lists are ideal
"""


# Using built in `heapq` library
import heapq


# ------------ Min Heap ------------------------

A = [3, 2, 6, 0, -1, -2, -4]
print('Original random array: ', A)
'''
             3
        2         6
     0   -1    -2   -4
'''

# Heapify
heapq.heapify(A)
print('\nMin heapified array: ', A)
'''
             -4
        -1         -2
     0    2      3     6
'''

# Heap push
heapq.heappush(A, 8)
print('\nHeap push 8: ', A)
'''
             -4
        -1         -2
     0    2      3     6
   8
'''


# Heap pop
minn = heapq.heappop(A)
print('\nHeap pop: ', minn)
minn = heapq.heappop(A)
print('Heap pop: ', minn)
minn = heapq.heappop(A)
print('Heap pop: ', minn)


# Heap peek
print('\nHeap peek: ', A[0])
print(A)


# Heap pushpop
# heapq library supports pushing and popping in the same operation
A2 = [6, 1, 2, -3, 0, -8]
print('\nHeap pushpop')
print('Original array: ', A2)
heapq.heapify(A2)
print('Min heapified array: ', A2)

heapq.heappushpop(A2, -1)
print('Pop min, Push -1: ', A2)



# ------------ Heap Sort ------------------------
def heapsort(arr: list) -> list:
	"""
	Time: O(n * log n)
	Space: O(n)  | this can be done in O(1), but that code is slightly more complex
	"""
	heapq.heapify(arr)  # min heapify the array
	sorted = [0]*len(arr)  # slightly more time efficient approach (prevent resizing with appends)
	n = len(arr)

	for i in range(n):  # Looping n times
		sorted[i] = heapq.heappop(arr)  # Heappop will fix the heap, which is log n time

	return sorted

print('\nHeap sort')
A3 = [-2, 1, 7, 9, 2, 11, -3, -7, 2, 8, 3]
print('Original heap: ', A3)
B = heapsort(A3)
print('Sorted heap: ', B)



# ------------ Max Heap ------------------------
# requires Python 3.14 (new feature)

# For Python <3.14, a workaround is to negate all the
# values in your array and use a standard min heap
