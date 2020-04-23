# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-23

# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
# (结果可能会很大，你需要将结果模上1000000007)

from typing import *
import functools


class Solution:
    def waysToChange(self, n: int) -> int:
        # 思路1：动态规划
        # 状态方程 dp[i] = dp[i-1]+dp[i-5]+dp[i-10]+dp[i-25]
        coins = [25, 10, 5, 1]
        dp = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]
        return dp[n] % 1000000007

        # 思路2：数学方法
        # mod = 10 ** 9 + 7
        #
        # ans = 0
        # for i in range(n // 25 + 1):
        #     rest = n - i * 25
        #     a, b = rest // 10, rest % 10 // 5
        #     ans += (a + 1) * (a + b + 1)
        # return ans % mod


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 101):
        print(i, s.waysToChange(i))
