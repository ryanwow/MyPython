# https://leetcode.cn/problems/spiral-matrix-ii/description/
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        step = 1
        row_top, row_bottom, col_left, col_right = 0, n - 1, 0, n - 1
        index = 1
        while index <= n * n:
            match step:
                case 1:
                    for i in range(col_left, col_right + 1):
                        result[row_top][i] = index
                        index += 1
                    row_top += 1
                    step = 2
                case 2:
                    for i in range(row_top, row_bottom + 1):
                        result[i][col_right] = index
                        index += 1
                    col_right -= 1
                    step = 3
                case 3:
                    for i in range(col_right, col_left - 1, -1):
                        result[row_bottom][i] = index
                        index += 1
                    row_bottom -= 1
                    step = 4
                case 4:
                    for i in range(row_bottom, row_top - 1, -1):
                        result[i][col_left] = index
                        index += 1
                    col_left += 1
                    step = 1
        return result


if __name__ == '__main__':
    n = 3
    s = Solution()
    result = s.generateMatrix(n)
    print(result)