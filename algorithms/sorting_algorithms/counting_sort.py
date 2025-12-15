'''
Counting Sort

Calculate the frequency of each value in the array, then use that 
to reconstruct the array in sorted order.
'''


def counting_sort(arr: list):
    '''Assuming an array of positive integers'''
    
    # Get max value
    max_value = max(arr)
            
    # Initialize counts array
    counts = [0] * (max_value+1)
    
    # Calculate frequencies
    for num in arr:
        counts[num] += 1
        
    # Update the original array in-place
    i, j = 0, 0
    n = len(arr)
    while i < n:  # Loop going through original array
        while counts[j] > 0:  # Loop going through counts array
            arr[i] = j
            i += 1
            counts[j] -= 1
        j += 1
            
    
arr = [6, 2, 8, 5, 2, 1, 4, 9, 4, 2, 3, 6, 7, 1, 0, 7, 4, 1]
print('Original array: ', arr)
counting_sort(arr)
print('Sorted array: ', arr)
