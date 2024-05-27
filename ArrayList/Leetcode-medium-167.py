# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers)
        while i < j:
            add = numbers[i - 1] + numbers[j - 1]
            if add == target:
                return [i, j]
            elif add > target:
                j -= 1
            elif add < target:
                i += 1
            else:
                continue
        return [i, j]


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(numbers, target)
    print(res)
