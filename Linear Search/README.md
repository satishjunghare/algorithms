# Linear Search
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

## Example :
```
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
            x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
            x = 175;
Output : -1
Element x is not present in arr[].
```

A simple approach is to do a linear search, i.e  

1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return -1.


## Output :
```
Element is present at index 5
```