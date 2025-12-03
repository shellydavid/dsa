
def binary_search(arr: list, target: int) -> int:
	'''
	Return the index of target if found.
	Return -1 if not found
	'''
	l = 0
	r = len(arr)-1

	while l <= r:  # Break out of the loop once the indices criss-cross (indicates search space was unsuccessfully exhausted)
		m = (r+l) // 2
		if arr[m] > target: # Target is to the left (less)
			r = m-1
		elif arr[m] < target:  # Target is to the right (greater)
			l = m+1
		else:  # Target found
			return m

	return -1



arr = [-1,0,3,5,9,12]
print('\n------------------------')
print(arr)
print(f"Target: 9  | {binary_search(arr, 9)}")
print(f"Target: 2  | {binary_search(arr, 2)}")
print(f"Target: 5  | {binary_search(arr, 3)}")


arr = [2, 5]
print('\n------------------------')
print(arr)
print(f"Target: 0  | {binary_search(arr, 0)}")
print(f"Target: 2  | {binary_search(arr, 2)}")
print(f"Target: 5  | {binary_search(arr, 5)}")
