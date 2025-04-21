# Link:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1
        unique = 0

        while len(nums) > index:
            if nums[index] == nums[unique]:
                nums.pop(index)
            else:
                unique = index

            if index == unique:
                index += 1
        return index
