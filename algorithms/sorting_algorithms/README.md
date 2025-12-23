# Sorting Algorithms


## Bubble Sort - `O(n^2)`

1. Iterate through the array, compare two neighboring elements, and swap them if the order is incorrect. 
2. Repeat multiple iterations over the array until it's sorted 

The highest elements "bubble" up into their correct position

<img height=200 width=500 src=https://media.geeksforgeeks.org/wp-content/uploads/20190704131909/bubblusort.gif>


## Counting Sort - `O(k+n)`

#### Algorithm

*(Assuming an array of positive integers for this case)*

Track the *frequency* of each element in the array, then use that to reconstruct the array in sorted order

1. Find the maximum value `k`
2. Create a `counts` array with `k+1` indices, initialized with 0s
3. Iterate through the original array, and increment it's index in `counts`
4. Reconstruct the original array in-place

#### Complexity
* **Time**: traversing the input array to find the max is `O(n)`, and creating the `counts` array of size `k` is `O(k)`
* **Space**: since the input is modified in-place, the only extra space is the `counts` array of size `k`

**NOTE**: This algorithm is inefficient if `k` is big relative `n` (for ex, array has only 3 elements but the max value is 1 million)

<img src='../../img/counting-sort.png' height=400 width=700>


## Insertion Sort - `O(n^2)`

1. To start, the first element is considered the 'sorted region' and the rest of the array is the 'unsorted region'.
2. Iterate through the array and insert elements into the 'sorted region' in their correct position

<img src='../../img/insertion-sort.png' height=400 width=600>


## Merge Sort - `O(n logn)`

1. **Divide & Conquer**: divide the array into halves until you reach leaves (single length arrays), which are trivially sorted
2. **Merge** - merge the subarrays arrays back together in sorted order

Because the subarrays are sorted after each step, merging them is very efficient `O(n)`. You can simply compare indices and increment, iterating through each subarray only once (without having to go backwards or re-scan, like with bubble sort).

<img height=400 src=https://www.w3schools.com/dsa/img_mergesort_long.png>


## Quick Sort - `O(n logn)`

Divide & Conquer algorithm that recursively selects a 'pivot' *(element in the array)* and splits the array into 3 sub-arrays:
- Elements <= the pivot
- The pivot itself
- Elements > the pivot

Once all final base cases are reached, the sub-arrays are simply concatenated together

**Time complexity breakdown**:
 - `O(n)`: scanning the array to compare elements against the pivot
 - `O(logn)`: recursively diving the array
        
**NOTE**: *A bad pivot will have `O(n^2)` overall complexity*

<img src='../../img/quick-sort.webp' height=350 width=400>


## Selection Sort - `O(n^2)`

1. Begin at the first index and traverse the rest of the array to find the minimum value
2. Replace the first index with the minimum value found
3. Move to the next index and repeat

Similar to Insertion Sort, there is a 'sorted' and 'unsorted' portion of the array. As you iterate through the array, you select the minimum value from the unsorted region and swap it with the first element in the unsorted region (which should be your current index). 

<img src='../../img/selection-sort.jpg' height=350 width=400>
