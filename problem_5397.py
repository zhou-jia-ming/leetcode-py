# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-17

# 最简分数
# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简分数。
# 分数可以以 任意 顺序返回。

from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # 周赛第二题， 最简分数的本质是两个数的最小公约数等于1. 两层循环O(n^2)
        if n < 2:
            return []
        res = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if i == j:
                    continue
                if gcd(i, j) == 1:
                    res.append("{}/{}".format(i, j))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.simplifiedFractions(4))
