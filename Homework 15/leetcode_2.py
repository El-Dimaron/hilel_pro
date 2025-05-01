# Link:
# https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s[::-1].split(maxsplit=1)[0][::-1].strip())
