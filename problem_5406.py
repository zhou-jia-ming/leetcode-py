# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-10

# 收集树上所有苹果的最少时间
# 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。
# 通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，
# 可以收集到所有苹果，并回到节点 0 。
#
# 无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。
# 除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *

from functools import lru_cache


class TreeNode(object):
    def __init__(self, val, left, right, hasApple):
        self.val = val
        self.left = left
        self.right = right
        self.hasApple = hasApple


class Solution:
    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        # 周赛第3题。
        # 思路，用后序遍历二叉树的方法进行累计，如果子树没有苹果返回-1，
        # 收集苹果的最少时间等于有苹果的子树路径和+1的2倍。
        my_dict = {}
        for s, e in edges:
            if s in my_dict:
                my_dict[s].append(e)
            else:
                my_dict[s] = [e]
        res = 0

        if not my_dict:
            return res

        @lru_cache(None)
        def dfs(i):
            if i not in my_dict and not hasApple[i]:
                return -1
            subs = [0]
            if i in my_dict:
                for sub in my_dict[i]:
                    if dfs(sub) != -1:
                        subs.append(dfs(sub))
            subs = sum(subs)
            if not subs:
                return -1 if not hasApple[i] else 1
            return subs + 1

        # dfs, 如果左节点有苹果就返回最小路径 没有返回-1

        return 2 * sum([dfs(sub) for sub in my_dict[0] if dfs(sub) != -1])


if __name__ == "__main__":
    s = Solution()
    false = False
    true = True
    print(
        s.minTime(7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                  hasApple=[false, false, true, false, true, true, false]))
