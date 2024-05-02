# https://leetcode.cn/problems/diagonal-traverse/description/
# steps:
# 1: x+1,y-1 ; 2: x+1,y ; 3: x-1,y+1 ; 4: x,y+1
# 因为不可以逆行，所以
# 如果step_last=1而且step2不可执行，跳过step3
# 如果step_last=3而且step4不可执行，跳过step1


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m = len(mat)
        if m <= 0:
            return result
        n = len(mat[0])
        x = 0
        y = 0
        step_last = 0
        for i in range(m * n):
            result.append(mat[x][y])
            moved = 0
            if step_last == 1 or step_last == 3:
                step_start = step_last
            elif step_last == 2:
                step_start = 3
            else:
                step_start = 1
            for j in range(4):
                step = step_start + j
                if step > 4:
                    step -= 4
                if step_last == 1 and step == 3:
                    continue
                if step_last == 3 and step == 1:
                    continue
                match step:
                    case 1:
                        if y + 1 < n and x - 1 >= 0:
                            y += 1
                            x -= 1
                            moved = 1
                    case 2:
                        if y + 1 < n:
                            y += 1
                            moved = 1
                    case 3:
                        if y - 1 >= 0 and x + 1 < m:
                            y -= 1
                            x += 1
                            moved = 1
                    case 4:
                        if x + 1 < m:
                            x += 1
                            moved = 1
                    case _:
                        print('no')
                if moved == 1:
                    step_last = step
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    mat = [[2,3]]
    r = s.findDiagonalOrder(mat)
    print(r)
