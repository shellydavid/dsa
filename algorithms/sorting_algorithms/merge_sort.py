'''
Merge Sort
A recursive/divide & conquer approach.

Divide - O(logn):
Keep dividing the array by half until you reach the base cases (single length arrays / leaf nodes)
	- log2(n) time, because you keep dividing by half

Conquer - O(n):
Traverse the leafs at each level and sort them while merging them
	- O(n) time, because at each level in the tree you effectively traverse all items in the array

Time complexity: O(n logn)
Space complexity: can be O(n) or O(logn) - the latter is more complex to implement
'''

# Recursive approach using two functions
def merge_sort(arr: list):
	n = len(arr)

	if n == 1:
		return arr

	M = n // 2
	R = arr[M:]
	L = arr[:M]

	r = merge_sort(R)
	l = merge_sort(L)

	return merge(l, r)

def merge(L: list, R: list):
	result = []
	l, r = 0, 0

	while l < len(L) and r < len(R):
		if L[l] < R[r]:
			result.append(L[l])
			l += 1
		else:
			result.append(R[r])
			r += 1

	while l < len(L):
		result.append(L[l])
		l += 1

	while r < len(R):
		result.append(R[r])
		r += 1

	return result


array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print('Original array: ', array)
print('Sorted array: ', merge_sort(array))
