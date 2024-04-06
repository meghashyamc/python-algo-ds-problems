from typing import List

# Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.

# For this problem, return the indices of maximum continuous series of 1s in order.

# If there are multiple possible solutions, return the sequence which has the minimum start index.



# Problem Constraints
#  0 <= B <= 10^5

#  1 <= size(A) <= 10^5

#  0 <= A[i] <= 1



# Input Format
# First argument is an binary array A.

# Second argument is an integer B.



# Output Format
#  Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.



# Example Input
# Input 1:

#  A = [1 1 0 1 1 0 0 1 1 1 ]
#  B = 1
# Input 2:

#  A = [1, 0, 0, 0, 1, 0, 1]
#  B = 2


# Example Output
# Output 1:

#  [0, 1, 2, 3, 4]
# Output 2:

#  [3, 4, 5, 6]


# Example Explanation
# Explanation 1:

#  Flipping 0 present at index 2 gives us the longest continous series of 1's i.e subarray [0:4].
# Explanation 2:

#  Flipping 0 present at index 3 and index 5 gives us the longest continous series of 1's i.e subarray [3:6].
#  Problem source: interviewbit.com 


def get_max_continuous_ones_after_flipping_zeroes(arr: List[int], max_zero_flips:  int) -> List[int]:
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [1]
    if len(arr) == 2:
        return [0,1]
    start = 0
    end = 0
    min_index_for_continuous_ones = -1
    max_index_for_continuous_ones = -1
    available_zeroes_to_flip = max_zero_flips

    while start <= len(arr)-1 and start >=0 and end <=len(arr) and end >=0 and start <= end:

        if end == len(arr) or arr[end] == 0:
            if available_zeroes_to_flip == 0 or end == len(arr):
                if end-start > max_index_for_continuous_ones-min_index_for_continuous_ones:
                    min_index_for_continuous_ones = start
                    max_index_for_continuous_ones = end
                if arr[start] == 0 and max_zero_flips > 0:
                    available_zeroes_to_flip +=1
                if start == end:
                    end += 1
                start += 1
                continue
            available_zeroes_to_flip -= 1
            end += 1
            continue
        end += 1
        continue

    max_continuous_ones_arr = []
    i = min_index_for_continuous_ones

    while i < max_index_for_continuous_ones:
      max_continuous_ones_arr.append(i) 
      i += 1
    
    return max_continuous_ones_arr


            







