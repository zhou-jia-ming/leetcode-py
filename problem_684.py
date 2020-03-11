# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 在本问题中, 树指的是一个连通且无环的无向图。
#
# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
#
# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/redundant-connection
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class disjoint(object):
    def __init__(self, length):
        self.array = [-1] * length

    def find(self, i):
        while self.array[i] != -1:
            i = self.array[i]
        return i

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if (x != y) or (x == -1 and y == -1):
            self.array[x] = y


class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        a = set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])
        tree = disjoint(len(a) + 1)
        ans = None
        for i in edges:
            x = tree.find(i[0])
            y = tree.find(i[1])
            if (x != y) or (x == -1 and y == -1):
                tree.union(i[0], i[1])
            else:
                ans = i
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
