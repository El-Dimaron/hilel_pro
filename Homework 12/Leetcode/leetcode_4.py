# Link:
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        unique = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[unique] = nums[index]
                unique += 1
        return unique
