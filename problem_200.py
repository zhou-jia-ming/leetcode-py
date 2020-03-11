# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-25


# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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

    def number(self):
        s = set()
        for i, item in enumerate(self.array):
            if i == item or item == -1:
                pass
            else:
                s.add(self.find(i))
        return len(s)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        dsu = disjoint(width * height)
        single_land = 0
        for i, line in enumerate(grid):
            for j, item in enumerate(line):
                if item == '1':
                    pos = i * width + j
                    flag = True
                    if 0 <= i + 1 < height and grid[i + 1][j] == '1':
                        pos_right = (i + 1) * width + j
                        dsu.union(pos, pos_right)
                        flag = False

                    if 0 <= i - 1 < height and grid[i - 1][j] == '1':
                        pos_left = (i - 1) * width + j
                        dsu.union(pos, pos_left)
                        flag = False
                    if 0 <= j - 1 < width and grid[i][j - 1] == '1':
                        pos_up = i * width + j - 1
                        dsu.union(pos, pos_up)
                        flag = False
                    if 0 <= j + 1 < width and grid[i][j + 1] == '1':
                        pos_down = i * width + j + 1
                        dsu.union(pos, pos_down)
                        flag = False
                    if flag:
                        single_land += 1

        return dsu.number() + single_land


if __name__ == "__main__":
    s = Solution()
    # print(s.numIslands(
    #     [["1", "1", "1", "1", "0"],
    #      ["1", "1", "0", "1", "0"],
    #      ["1", "1", "0", "0", "0"],
    #      ["0", "0", "0", "0", "0"]]))
    print(s.numIslands([["1", "1", "0", "0", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "1", "0", "0"],
                        ["0", "0", "0", "1", "1"]]))
