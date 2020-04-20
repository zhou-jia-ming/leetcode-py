# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-20

# 有 N 个网络节点，标记为 1 到 N。
#
# 给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。
#
# 现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/network-delay-time
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *

import heapq, collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 深度优先遍历+记忆化剪枝
        # from collections import defaultdict
        # graph = defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append((w, v))
        #
        # dist = {node: float("inf") for node in range(1, N + 1)}
        #
        # def dfs(node, elapsed):
        #     if elapsed >= dist[node]:  # 如果该节点有更早的访问时间，不广播
        #         return
        #     dist[node] = elapsed  # 记录第一次访问时间
        #     for time, nei in graph[node]:
        #         # 广播
        #         dfs(nei, elapsed + time)
        #
        # dfs(K, 0)
        # ans = max(dist.values())
        # return -1 if ans == float("inf") else ans

        # 单源最短路算法 快了10倍
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]  # 堆，保存最短路,每次弹出最小值来更新最短路
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                # 不访问已经访问过的点
                continue
            dist[node] = d  # 更新点信息
            for nei, d2 in graph[node]:
                # 遍历当前点的邻接点。如果没访问过，push到堆
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1


if __name__ == "__main__":
    s = Solution()
    print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
