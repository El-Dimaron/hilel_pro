# Link:
# https://leetcode.com/problems/valid-parentheses/

from collections import deque


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = deque()

        brackets_dict = {
            "[": "]",
            "{": "}",
            "(": ")"}

        for bracket in s:
            if bracket in brackets_dict:
                stack.append(bracket)

            else:
                if stack:
                    if brackets_dict.get(stack.pop()) != bracket:
                        return False
                else:
                    return False

        return not bool(stack)
