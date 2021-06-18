# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true


# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse = str_x[::-1]
        if str_x == reverse:
            return True
        else:
            return False
