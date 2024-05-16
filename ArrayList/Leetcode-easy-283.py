# https://leetcode.cn/problems/move-zeroes/description/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
             return
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,1,2]
    s.moveZeroes(nums)
    print(nums)