# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-16

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
# 你需要让组成和的完全平方数的个数最少。

import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0
        # 递推，f(n) = min(f(n-k)) # k=1,4,9,16...
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(100))
