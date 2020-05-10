# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-10

# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和
#  '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。
#
# 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，
# 将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，
# 那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。
#
# 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，
# 请你返回它对 10^9 + 7 取余的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *

from functools import lru_cache


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 周赛第四题，前面debug时间太多，这道题没时间写。
        # 思路，深度优先搜索+记忆化
        # 总结一下，这道题的深度搜索是用最后一块是否有苹果做递归出口的。
        # 递归条件是能继续切（满足切下部位有苹果）切到最后有苹果，结果+1
        row, col = len(pizza), len(pizza[0])

        @lru_cache(None)
        def dfs(x, y, k):
            if not k:
                # 如果k==0表示,不需要切，判断剩下部分是否有苹果。
                return any('A' in p[y:col] for p in pizza[x:row])
            res = 0
            # 先竖着切.
            for i in range(x + 1, row):
                if any('A' in p[y:col] for p in pizza[x:i]):
                    res += dfs(i, y, k - 1)
            # 在横着切。
            for j in range(y + 1, col):
                if any('A' in p[y:j] for p in pizza[x:row]):
                    res += dfs(x, j, k - 1)
            # 返回切法。
            return res

        return dfs(0, 0, k - 1) % 1000000007


if __name__ == "__main__":
    s = Solution()
    print(s.ways(["A..", "AAA", "..."], 3))
