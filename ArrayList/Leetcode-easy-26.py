# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
            elif nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)



if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    res = s.removeDuplicates(nums)
    print(nums)
    print(res)
