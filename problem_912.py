# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-31

# 给你一个整数数组 nums，请你将该数组升序排列。
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 每日一签
        # 手写快排
        def qs(data):
            if not data:
                return list()
            res = [data[0]]
            left = qs([d for d in data[1:] if d < data[0]])
            right = qs([d for d in data[1:] if d >= data[0]])
            return left + res + right
        return qs(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 1, 1, 2, 0, 0]))
