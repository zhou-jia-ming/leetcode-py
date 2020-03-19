# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-19

from typing import List


# 有一堆石头，每块石头的重量都是正整数。
#
# 每一回合，从中选出两块最重的石头，然后将它们一起粉碎。
# 假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 模拟流程，排序，
        # 每次取出最大和次大，比较，插入y-x,继续取最大和次大，直到剩下0个石头或者1个石头
        from bisect import bisect_left
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x == y:
                continue
            else:
                rest = y - x
                index = bisect_left(stones, rest)
                stones.insert(index, rest)
        if len(stones) == 0:
            return 0
        return stones[0]


if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
