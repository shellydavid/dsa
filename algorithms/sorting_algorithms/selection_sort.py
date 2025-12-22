'''
Selection Sort


1. Begin at the first index and traverse the array to find the minimum value
2. Replace the first index with the minimum value
3. Repeat

The minimum values are selected from the unsorted region and swapped into their correct position.
'''


# Time complexity: O(n^2)
# Space complexity: O(1)
def selection_sort(arr: list):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:  # Find the index with the smallest value in the remaining portion of the array
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap their positions
    


arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print('Original array: ', arr)
selection_sort(arr)
print('Sorted array: ', arr)
