# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-22

# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：
#
# 1 表示连接左单元格和右单元格的街道。
# 2 表示连接上单元格和下单元格的街道。
# 3 表示连接左单元格和下单元格的街道。
# 4 表示连接右单元格和下单元格的街道。
# 5 表示连接左单元格和上单元格的街道。
# 6 表示连接右单元格和上单元格的街道。
# 你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。
#
# 注意：你 不能 变更街道。
#
# 如果网格中存在有效的路径，则返回 true，否则返回 false 。

from typing import List


class disjoint(object):
    def __init__(self, length):
        self.array = [-1 for _ in range(length)]

    def find(self, i):
        while self.array[i] != -1:
            i = self.array[i]
        return i

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if (x != y) or (x == -1 and y == -1):
            self.array[x] = y


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 其实大多数人用的DFS，其实dfs更好写一点。
        # 并查集算法，连通各个网格，判断0->grid[-1][-1]是否连通
        h = len(grid)
        w = len(grid[0])
        dis = disjoint(h * w)
        num = -1
        for y, line in enumerate(grid):
            for x, item in enumerate(line):
                num += 1
                if item in (1, 4, 6):
                    if x + 1 < w:
                        right = grid[y][x + 1]
                        if right in (1, 3, 5):
                            dis.union(num, num + 1)
                if item in (2, 3, 4):
                    if y + 1 < h:
                        down = grid[y + 1][x]
                        if down in (2, 5, 6):
                            dis.union(num, num + w)

        x = dis.find(0)
        y = dis.find(len(dis.array) - 1)
        if x != y or (x == -1 and y == -1):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.hasValidPath([[2, 4, 3], [6, 5, 2]]))
    print(s.hasValidPath([[1, 1, 1, 1, 1, 1, 3]]))
    print(s.hasValidPath([[2], [2], [2], [2], [2], [2], [6]]))
    print(s.hasValidPath([[2, 4, 3], [6, 5, 2]]))
    print(s.hasValidPath([[1, 2, 1], [1, 2, 1]]))

