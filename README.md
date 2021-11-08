# Algorithm_Examples

This is a list of popular algorithms taken from LeetCode and other sources. 

Look descr.pdf for some more details.

## Binary Search

Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array.  If the target value is greater than the element, the search continues in the upper half of the array. 

Complexity: O(log(n))

# Bit Manipulation

Sometimes binary representation of numbers can be helpdul for comparisons and calculations.


## Dynamic Programming

It refers to simplifying a complicated problem by breaking it down into simpler sub-problems. Problem is expected to be solved by breaking it into sub-problems and then recursively finding the optimal solutions.

## Hash Function

A hash function is any function that can be used to map data of arbitrary size to fixed-size values. 

## Sorting

### Bubble Sort

We look at pairs of adjacent elements in an array, one pair at a time, and swap their positions if the first element is larger than the second, or simply move on if it isn't.

### Quick Sort

Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot. Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it. This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

### Counting Sort

Unsorted array a[0],..., a[n-1], where |a[j]| < k

 It operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence. An auxiliary array used first to store the numbers of items with each key, and then (after the second loop) to store the positions where items with each key should be placed.

Complexity O(n+k)

Extra memory: k

## Two Pointers

These kind of problems usually involve two pointers: One slow-runner and the other fast-runner.

There is another variation: One pointer starts from the beginning while the other pointer starts from the end.
