# https://leetcode.cn/problems/find-pivot-index/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        sums = []
        s = 0
        length = len(nums)
        for i in range(length):
            s += nums[i]
            sums.append(s)
        for i in range(length):
            if (((i == 0 or i == length - 1) and (sums[length - 1] - nums[i] == 0))
                    or (sums[i] - nums[i]) * 2 == sums[length - 1] - nums[i]):
                res = i
                break
        return res


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    nums = [2, 1, -1]
    result = s.pivotIndex(nums)
    print(result)

