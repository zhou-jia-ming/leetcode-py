# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-19

from typing import List


# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 思路： 递推解法，类似于斐波那契数列

        dp = [0 for _ in range(len(cost)+1)]

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[len(cost)]


if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
