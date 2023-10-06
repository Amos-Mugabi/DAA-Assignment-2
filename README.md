# DAA-Assignment-2

1. Quick Sort
This refers to a sorting algorithm that uses a divide-and-conquer approach to sort an array or a list of elements.
QuickSort Algorithm:

Choose a pivot element from the array.
Partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
Recursively sort the sub-arrays.
Join the sub-arrays and the pivot back into a single sorted array.

A diagram to illustrate quick sort.
![quicksort img](https://github.com/Amos-Mugabi/DAA-Assignment-2/assets/115138015/20424ac1-19df-4b5a-a0fd-8b7a264d9452)




Explanation:

In this example, the quicksort function takes a list as input and recursively sorts it using the QuickSort algorithm. 
The pivot is chosen as the first element of the input list. 
Elements less than or equal to the pivot are placed in the less list, and elements greater than 
the pivot are placed in the greater list. The function then recursively calls itself on the less and greater 
lists and concatenates the sorted sublists along with the pivot to produce the final sorted list.

Analysis:

QuickSort is a highly efficient and widely used sorting algorithm with an average-case time complexity of O(n log n). 
It is faster than many other sorting algorithms, especially for large datasets. 
However, its performance highly depends on the choice of the pivot element. 
Randomized algorithms can be employed to improve the average-case time complexity and mitigate the risk of worst-case behavior. 
While it is not stable, QuickSort's balance of average-case performance and simplicity makes it a popular choice in practice.





Counting Sort:

This refers to an efficient sorting algorithm that works by counting the number of occurrences of each 
element in the input array and using this information to place the elements in sorted order. 

Counting Phase: Count the number of occurrences of each element and store the count in an auxiliary array, 
often referred to as the counting array.

A diagram to illustrate counting sort.
![countingsort img](https://github.com/Amos-Mugabi/DAA-Assignment-2/assets/115138015/3a47f7e7-c330-44b7-a6fa-62f0ae9b0ea9)


Analysis:
Counting sort is a linear time complexity sorting algorithm suitable for sorting integers within a limited range. 
It is efficient and simple, but its main limitation is its space complexity, 
which makes it less suitable for sorting large datasets with a wide range of values.




Heap Sort:

This refers to a comparison-based sorting algorithm that uses a binary heap data structure to
 build a max-heap (for ascending order) or a min-heap (for descending order) and then sorts the elements.

Build a Max-Heap: Convert the given array into a binary heap, a complete binary tree where every node 
is greater than or equal to its children (max-heap property). 
Start from the last non-leaf node and move up,
ensuring that the max-heap property is maintained at every step.
Heapify: Repeatedly remove the maximum element (root of the heap) and replace it with the last element of the heap, 
then heapify the heap again to maintain the max-heap property.
Repeat: Continue this process until the heap size is reduced to 1. 
The remaining element will be the sorted array.

A diagram to illustrate heap sort.
<img width="614" alt="heapsort img" src="https://github.com/Amos-Mugabi/DAA-Assignment-2/assets/115138015/07886d11-1f69-4732-bb01-aa7621a1af0a">

Explanation:

This function takes an array arr, its size n, and an index i.
It assumes that the binary trees rooted at left child (2i + 1) and right child (2i + 2) are max heaps, 
but the tree rooted at index i might not be a max heap.
heapify() compares the value at index i with its left and right children and finds the largest among the three elements.
If the largest element is not at index i, it swaps the elements and recursively calls heapify() 
on the affected child to maintain the max heap property.

Analysis:

 Heap Sort is an efficient and comparison-based sorting algorithm with a 
 time complexity of O(n log n) and a space complexity of O(1). 
 It is particularly useful when you need a stable sort and when the input data is too large to fit in memory, 
 as it sorts elements in place without the need for additional memory proportional to the input size.




