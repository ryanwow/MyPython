# https://leetcode.cn/problems/remove-element/description/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p, q = 0, 0
        length = len(nums)
        while p < length and q < length:
            if nums[p] == val:
                if nums[q] != val:
                    nums[p], nums[q] = nums[q], nums[p]
                    p += 1
                    q += 1
                else:
                    q += 1
            else:
                p += 1
                q += 1
        count = 0
        for i in range(length):
            if nums[i] == val:
                count += 1
        return length - count


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    val = 1
    res = s.removeElement(nums, val)
    print(res)
    print(nums)