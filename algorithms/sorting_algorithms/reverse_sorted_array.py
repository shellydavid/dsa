"""
Two-pointer approach, modifying array in-place

Time: O(n)
Space: O(1)
"""

def reverse(arr: list):
	l = 0
	r = len(arr)-1

	while l < r:
		arr[l], arr[r] = arr[r], arr[l]
		l += 1
		r -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(arr)
print(arr)
