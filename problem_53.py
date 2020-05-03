# coding:utf-8
# Created by: Jiaming
# Created at:

from typing import *


# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），
# 返回其最大和。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 思路,遍历时维护一个包含当前数字的子数组的和。
        # 如果当前和大于0，加上n， ps.相当于子数组右边扩展一位。
        # 如果小于0，子数组从n开始，总数等于n.
        # n以前的最大和小于0，则最大子数组不可能加上小于0的和
        # 更新当前最大值。
        res = float("-inf")
        total = 0
        for n in nums:
            if total > 0:
                total += n
            else:
                total = n
            res = max(res, total)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
