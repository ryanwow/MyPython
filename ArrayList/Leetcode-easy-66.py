# https://leetcode.cn/problems/plus-one/


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        flag = 1
        length = len(digits)
        for i in range(length):
            temp = digits[length - 1 - i] + flag
            if temp > 9:
                flag = 1
                ans = temp % 10
                result.insert(0, ans)
            else:
                flag = 0
                result.insert(0, temp)
        if flag == 1:
            result.insert(0, 1)
        return result


if __name__ == '__main__':
    s = Solution()
    digits = [9, 9]
    res = s.plusOne(digits)
    print(res)

