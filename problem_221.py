# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-08

# 最大正方形
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 求最大正方形面积等于求最大边长, dp[i][j]表示mat[i][j]为右下角的最大正方形边长。
        # 考虑dp[i][j] = min(dp[i-1][j-1,dp[i-1][j],dp[i][j-1])
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:

                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1],
                                       dp[i - 1][j]) + 1
        # from pprint import pprint
        # pprint(dp)
        return max(map(max, dp)) ** 2


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["1", "0", "1", "0", "0"],
                           ["1", "0", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"],
                           ["1", "0", "0", "1", "0"]]))
