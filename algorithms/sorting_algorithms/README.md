# Sorting Algorithms


## Bubble Sort - `O(n^2)`

1. Iterate through the array, compare two neighboring elements, and swap them if the order is incorrect. 
2. Repeat multiple iterations over the array until it's sorted 

The highest elements "bubble" up into their correct position

<img height=200 width=500 src=https://media.geeksforgeeks.org/wp-content/uploads/20190704131909/bubblusort.gif>


## Counting Sort


## Insertion Sort


## Merge Sort - `O(n logn)`

1. **Divide & Conquer**: divide the array into halves until you reach leaves (single length arrays), which are trivially sorted
2. **Merge** - merge the subarrays arrays back together in sorted order

Because the subarrays are sorted after each step, merging them is very efficient O(n). You can simply compare indices and increment, iterating through each subarray only once (without having to go backwards or re-scan, like with bubble sort).

<img height=400 src=https://www.w3schools.com/dsa/img_mergesort_long.png>


## Quick Sort


## Selection Sort