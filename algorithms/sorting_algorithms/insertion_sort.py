'''
Insertion sort

To start, the first element of the array is the 'sorted region' and the rest is the 'unsorted region'. 
Iterate through the unsorted region (right side of the array) and insert elements into the sorted region (left side of the array). 
'''


# Time complexity: O(n^2)
# Space complexity: O(1)
def insertion_sort(arr: list):
    n = len(arr)
    
    for i in range(1, n):  # Loop through unsorted region (R)
        for j in range(i, 0, -1):  # Loop through sorted region (L)
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]  # Insert element into correct spot in sorted region
            else:
                break  # If current indices are not out of order, there is no need to keep checking bec the region is sorted

        
arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print('Original array: ', arr)
insertion_sort(arr)
print('Sorted array: ', arr)
