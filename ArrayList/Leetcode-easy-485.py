# https://leetcode.cn/problems/max-consecutive-ones/description/


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        count_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count_max = max(count, count_max)
                count = 0
        return max(count_max, count)


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,1,0,1]
    result = s.findMaxConsecutiveOnes(nums)
    print(result)
