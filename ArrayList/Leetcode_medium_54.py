# https://leetcode.cn/problems/spiral-matrix/description/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        # step = 1 go right, 2 go down, 3 go left, 4 go up
        step = 1
        row_top, row_bottom, col_left, col_right = 0, m - 1, 0, n - 1
        count = 0
        while count < m * n:
            match step:
                case 1:
                    for i in range(col_left, col_right + 1):
                        result.append(matrix[row_top][i])
                    row_top += 1
                    step = 2
                case 2:
                    for i in range(row_top, row_bottom + 1):
                        result.append(matrix[i][col_right])
                    col_right -= 1
                    step = 3
                case 3:
                    for i in range(col_right, col_left - 1, -1):
                        result.append(matrix[row_bottom][i])
                    row_bottom -= 1
                    step = 4
                case 4:
                    for i in range(row_bottom, row_top - 1, -1):
                        result.append(matrix[i][col_left])
                    col_left += 1
                    step = 1
            count = len(result)
        return result


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    result = s.spiralOrder(matrix)
    print(result)
