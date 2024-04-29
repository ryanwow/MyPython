# https://leetcode.cn/problems/rotate-array/description/
# 有超大数组测试用例，会出现超时情况

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    print(nums)
