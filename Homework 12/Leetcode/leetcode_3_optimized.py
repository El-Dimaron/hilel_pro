# Link:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums: list[int]) -> int:
    unique = 1
    for index in range(1, len(nums)):
        if nums[index] != nums[index - 1]:
            nums[unique] = nums[index]
            unique += 1
    return unique
