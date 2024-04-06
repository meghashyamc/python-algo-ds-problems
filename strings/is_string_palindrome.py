
# Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

# Check the sample test case for reference.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Problem Constraints
# 1 <= |A| <= 10^6


# Input Format
# The first argument is a string A.


# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Example Input
# Input 1:
# "A man, a plan, a canal: Panama"
# Input 2:
# "race a car"


# Example Output
# Output 1:
# 1
# Output 2:
# 0


# Example Explanation
# Explanation 1:
# The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" 
# which is a palindrome after ignoring the case.
# Explanation 2:
# The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome
# Problem source: interviewbit.com 

def convert_to_alpha_numeric(s: str) -> str:

    alpha_numeric_str_parts = []

    for ch in s:
        if ch.isalnum():
            alpha_numeric_str_parts.append(ch)
    
    return "".join(alpha_numeric_str_parts).lower()



def is_string_palindrome(s: str) -> int:

    s = convert_to_alpha_numeric(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return 0
    return 1

