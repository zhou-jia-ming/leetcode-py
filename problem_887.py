# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-11

# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
#
# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
#
# 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
#
# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
#
# 你的目标是确切地知道 F 的值是多少。
#
# 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-egg-drop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        #  这是一道dp题，K个鸡蛋, 在每层扔一个鸡蛋。找出最大的，递归+记忆化，超时
        # mem = dict()
        #
        # def dp(egg, floor):
        #     if egg == 1: return floor
        #     if floor == 0: return 0
        #     if (egg, floor) in mem:
        #         return mem[(egg, floor)]
        #     res = float('INF')
        #     # 穷举所有可能的选择
        #     for i in range(1, floor + 1):
        #         res = min(res,
        #                   max(
        #                       dp(egg, floor - i),  # 没碎
        #                       dp(egg - 1, i - 1)  # 碎
        #                   ) + 1
        #                   )
        #     mem[(egg, floor)] = res
        #     return res
        #
        # return dp(K, N)

        # 优化一下
        @lru_cache(maxsize=100)
        def dp(k, n):
            if k == 1 or n == 1:
                # 一个鸡蛋，可以测n层，就是n次
                # 1次，只能测1层楼，
                # 加一方便编程
                return n + 1
            # 在n层扔鸡蛋
            # k-1,n-1表示第一个鸡蛋碎了，剩下k-1鸡蛋个扔n-1次能测的层数
            # k,n-1 表示没碎，k个鸡蛋测n-1次能测的层数。
            # 两者相加就是k个鸡蛋测n次的结果。
            # 原理是 如果鸡蛋没碎，只需测大于n的层数，测出来与鸡蛋碎了测n-1的相加
            # 就是总的层数
            return dp(k - 1, n - 1) + dp(k, n - 1)

        # dp表示k个鸡蛋扔i次最多可以测出多少层。

        for i in range(1, 200):
            if dp(K, i) >= N + 1:
                return i




if __name__ == "__main__":
    s = Solution()
    print(s.superEggDrop(4, 2000))
