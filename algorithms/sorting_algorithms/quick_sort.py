'''
Quick Sort

Divide & Conquer approach that recursively selects a pivot and creates 3 sub-arrays:
- [elements <= pivot]
- [pivot]
- [elements > pivot]

At the end, the sub-arrays are concatenated together and will be sorted
'''


# Time complexity: O(n logn)
# Space complexity: Can be O(1), code below is O(n)
def quick_sort(arr: list):

    # Base case
    if len(arr) <= 1:
        return arr
    
    # Create 3 sub-arrays based on pivot
    pivot = arr[-1]
    lte_pivot = [x for x in arr[:-1] if x <= pivot]
    gt_pivot = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(lte_pivot) + [pivot] + quick_sort(gt_pivot)
    

    
arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print('Original array: ', arr)
sorted_arr = quick_sort(arr)
print('Sorted array: ', sorted_arr)
