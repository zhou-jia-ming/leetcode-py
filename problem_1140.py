# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-22

# 亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。
# 游戏以谁手中的石子最多来决出胜负。
#
# 亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。
#
# 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。
# 然后，令 M = max(M, X)。
#
# 游戏一直持续到所有石子都被拿走。
#
# 假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。
from typing import *


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 思路，搜索+记忆化
        n = len(piles)
        mem = dict()
        s = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]
            # s[i]表示第i堆加上后边的堆的总数

        # dfs（i,M)表示从第i堆开始取的最优解
        def dfs(i, M):
            if (i, M) in mem:
                return mem[(i, M)]
            if i > n:
                # 没有石子
                return 0

            if M * 2 >= n - i:
                # 剩余堆小于2m, 全部取走
                return s[i]
            best = 0
            for x in range(1, M * 2 + 1):
                # 遍历x, s[i]减去对方的最优解，得到最大的就是本方的最优解
                best = max(best, s[i] - dfs(i + x, max(x, M)))
            mem[(i, M)] = best
            return best

        return dfs(0, 1)


if __name__ == "__main__":
    s = Solution()
    print(s.stoneGameII([2, 7, 9, 4, 4]))
