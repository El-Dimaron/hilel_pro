# Link:
# https://leetcode.com/problems/plus-one/

class Solution:
    @staticmethod
    def plusOne(digits: list[int]):
        r_index = len(digits) - 1
        digits[r_index] += 1

        while True:
            if digits[r_index] == 10 and r_index != 0:
                digits[r_index] = 0
                r_index -= 1
                digits[r_index] += 1
            elif digits[r_index] == 10 and r_index == 0:
                digits[r_index] = 0
                digits.insert(0, 1)
            else:
                return digits
