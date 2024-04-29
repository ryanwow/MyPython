# https://leetcode.cn/problems/product-of-array-except-self/description/
# 题目要求时间复杂度O(n)，有大数组用例，会出现超时，不可用两重循环计算

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer, left, right = [0] * length, [0] * length, [0] * length
        left[0] = 1
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(length):
            answer[i] = left[i] * right[i]
        return answer

if __name__ == '__main__':
    nums = [1,2,3,4]
    s = Solution()
    answer = s.productExceptSelf(nums)
    print(answer)
