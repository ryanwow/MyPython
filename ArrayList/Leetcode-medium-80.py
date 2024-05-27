# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        slow, fast = 2, 2
        while fast < length:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow



if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)
