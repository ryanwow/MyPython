# https://leetcode.cn/problems/set-matrix-zeroes/description/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        flag_row, flag_col = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flag_row[i] = True
                    flag_col[j] = True
        for i in range(m):
            for j in range(n):
                if flag_row[i] or flag_col[j]:
                    matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print(matrix)
