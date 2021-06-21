# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():  # [, {, ( の場合、stackに追加
                stack.append(char)
            elif char in dict.keys():  # ], }, ) の場合
                # 閉じカッコの前に開きカッコがない or 閉じカッコに対応する開きカッコが直前にない
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


