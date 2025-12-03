'''
Bubble Sort

At a given index, compare two numbers and determine if they need to be swapped.
Do multiple passes across the entire array, if needed

The highest values 'bubble' up into their correct spot
'''


# Implementation A: Inner and outer loop
def bubble_sort_a(arr):
	'''
	Time complexity:
		- Best case: O(n^2) the loop range is fixed and you iterate over the length n, n times (n*n)
		- Average case: O(n^2)
		- Worst case: O(n^2)
	Space complexity: O(1) - constant, since array is modified *in-place*. No additional mem used.
	'''
	n = len(arr)
	for i in range(n-1):  # Num of passes over the whole array (will be n-1, bec last number will be sorted each time)
		for j in range(n-1):  # Iterate through all values
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# Implementation A2: Inner loop enhancement
# 	After each pass, we know the highest number found will bubble to the top.
#	So after the first pass, we can stop comparing the last indices checked, since they are already sorted.
def bubble_sort_a2(arr):
	'''
	Time complexity:
		- Best case: O(n^2)
		- Average case: O(n^2)
		- Worst case: O(n^2)
	Space complexity: O(1)
	'''
	n = len(arr)
	for i in range(n-1):  # Num passes over whole array
		for j in range(n-i-1):  # Enhancement (minus 'i')
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# Implementation A3: Outer loop enhancement
# 	Early exit: If the list is already sorted, you do not need to keep repeating passes
def bubble_sort_a3(arr):
	'''
	Time complexity:
		- Best case: O(n)
		- Average case: O(n^2)
		- Worst case: O(n^2)
	Space complexity: O(1)
	'''
	n = len(arr)
	for i in range(n-1):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if not swapped:  # If no swaps occurred, you can stop the outer loop
			break


# Implementation B: While loop with early stop using boolean + swap count
def bubble_sort_b(arr):
	'''
	Time complexity:
		- Best case: O(n)
		- Average case: O(n^2)
		- Worst case: O(n^2)
	Space complexity: O(1) - now matter how big the array gets, you need the same number of`is_sorted` & `swap_count` variables
	'''
	is_sorted = False
	while not is_sorted:
		swap_count = 0
		for i in range(len(arr)-1):  # Can do range(1, len(arr)) or range(len(arr)-1)
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]  # Swap variables w/out a temp variable using tuple unpacking
				# Commas make a tuple, not parentheses-so 1, 2, 3 is the same as (1, 2, 3) with type <class 'tuple'>
				swap_count += 1
		if swap_count == 0:
			is_sorted = True


# Comparison
print('\n------------------------')
array = [1, 6, 2, 8, 2, 4, 5, 8, 3]
print('Method A')
print('Original array: ', array)
bubble_sort_a(array)
print('Final array: ', array)

print('\n------------------------')
array = [1, 6, 2, 8, 2, 4, 5, 8, 3]
print('Method A2')
print('Original array: ', array)
bubble_sort_a2(array)
print('Final array: ', array)

print('\n------------------------')
array = [1, 6, 2, 8, 2, 4, 5, 8, 3]
print('Method A3')
print('Original array: ', array)
bubble_sort_a3(array)
print('Final array: ', array)

print('\n------------------------')
array = [1, 6, 2, 8, 2, 4, 5, 8, 3]
print('Method B')
print('Original array: ', array)
bubble_sort_b(array)
print('Final array: ', array)
