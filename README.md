# Algorithm_Examples

This is a list of popular algorithms taken from LeetCode and other sources. 

Look descr.pdf for some more details.

## Binary Search

Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array.  If the target value is greater than the element, the search continues in the upper half of the array. 

Complexity: O(log(n))

## Counting sort

Unsorted array a[0],..., a[n-1], where |a[j]| < k

 It operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence. An auxiliary array used first to store the numbers of items with each key, and then (after the second loop) to store the positions where items with each key should be placed.

Complexity O(n+k)

Extra memory: k
