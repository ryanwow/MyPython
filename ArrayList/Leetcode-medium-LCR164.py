# https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/description/
from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        n = len(password)
        for i in range(n - 1):
            for j in range(n - i - 1):
                str1 = str(password[j])
                str2 = str(password[j + 1])
                if str1 + str2 > str2 + str1:
                    password[j], password[j + 1] = password[j + 1], password[j]
        result = ''
        for i in range(n):
            result += str(password[i])
        return result


if __name__ == '__main__':
    s = Solution()
    password = [15,8,7]
    result = s.crackPassword(password)
    print(result)