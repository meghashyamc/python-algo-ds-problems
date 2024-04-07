from typing import List
# Given a binary array, sort it using one traversal and no extra space

# Examples: 

# Input: 1 0 0 1 0 1 0 1 1 1 1 1 1 0 0 1 1 0 1 0 0 
# Output: 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
# Explanation: The output is a sorted array of 0 and 1

# Input: 1 0 1 0 1 0 1 0 
# Output: 0 0 0 0 1 1 1 1
# Explanation: The output is a sorted array of 0 and 1
# Source: https://www.geeksforgeeks.org/sort-binary-array-using-one-traversal/

def sort_binary_arr(arr: List[int]) -> List[int]:

    start = 0
    end = len(arr)-1
    while  start < end and start <= len(arr)-1 and end >= 0:
        if arr[start] == 0:
            start += 1
            continue
        while end > start and arr[end] != 0:
            end -= 1
        if arr[end] == 0:
            arr[start] = 0
            arr[end] = 1

    return arr



        