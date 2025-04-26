# Link:
# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l_edge = 0
        r_edge = len(nums) - 1

        while l_edge <= r_edge:
            mid = (l_edge + r_edge) // 2

            if nums[mid] == target:
                while True:
                    if mid == 0:
                        return mid
                    mid -= 1
                    if nums[mid] != target:
                        return mid + 1

            elif target < nums[mid]:
                r_edge = mid - 1
            elif target > nums[mid]:
                l_edge = mid + 1

        if target < nums[l_edge]:
            return l_edge
        return l_edge + 1
