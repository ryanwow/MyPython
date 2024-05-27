# https://leetcode.cn/problems/reverse-string/description/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    S = Solution()
    s = ['h', 'e', 'l', 'l', 'o']
    S.reverseString(s)
    print(s)
