
from typing import List,Dict
# Given an array of integers, find two numbers such that they add up to a specific target number.

 

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return an empty list.

# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.



# Problem Constraints
# 1 <= |A| <= 10^5
# -108 <= Ai <= 10^8
# -108 <= B <= 10^8


# Input Format
# The first argument is an integer array A.
# The second argument is an integer B.


# Output Format
# Return an array of integer, representing the answer


# Example Input
# A: [2, 7, 11, 15]
# B: 9


# Example Output
# [1, 2]


# Example Explanation
# The elements present at index 1 and index 2 add up to 9. i.e. A[1] + A[2] = 9 (1-based indexing)
# Source: interviewbit.com


def get_lowest_num_in_sorted_arr_greater_than_given_num(arr: List[int], num: int) -> int:
    for arr_num in arr:
        if arr_num - num > 0:
            return arr_num
    return num

    
def get_dict_of_arr_indices(arr: List[int]) -> Dict[int,List[int]]:
    arr_indices = {}
    for i in range(len(arr)):
        if arr[i] in arr_indices:
            arr_indices[arr[i]].append(i)
            continue
        arr_indices[arr[i]] = [i]
    return arr_indices
   
def get_numbers_with_given_sum(arr: List[int], target_sum: int) -> List[int]:
    if len(arr) < 2:
        return []

    nums_indices_dict = get_dict_of_arr_indices(arr)
 
    start_index_for_given_sum = -1
    end_index_for_given_sum = len(arr)

    for i in range(len(arr)):
        if target_sum - arr[i] in nums_indices_dict:
            index_of_needed_num = get_lowest_num_in_sorted_arr_greater_than_given_num(nums_indices_dict[target_sum - arr[i]], i)
            if index_of_needed_num > i:
                if (index_of_needed_num < end_index_for_given_sum) or ((index_of_needed_num == end_index_for_given_sum) and (i < start_index_for_given_sum)):
                    start_index_for_given_sum = i
                    end_index_for_given_sum = index_of_needed_num
    
    if start_index_for_given_sum == -1 or end_index_for_given_sum == len(arr):
        return []
    return [start_index_for_given_sum+1, end_index_for_given_sum+1]



        



