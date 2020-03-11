# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-04

# 在给定的网格中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotting-oranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 一次提交AC， 思路模拟腐蚀过程。
        count = 0
        self.grid = grid
        while self.has_fresh():
            print(self.grid)
            changed = self.spread()
            if not changed:
                break
            count += 1
        if self.has_fresh():
            return -1
        return count

    def spread(self):
        from copy import deepcopy
        new_grid = deepcopy(self.grid)
        changed = False
        for x, line in enumerate(self.grid):
            for y, item in enumerate(line):
                if item == 2:
                    if x - 1 > -1 and self.grid[x - 1][y] == 1:
                        new_grid[x - 1][y] = 2
                        changed = True
                    if x + 1 < len(self.grid) and self.grid[x + 1][y] == 1:
                        new_grid[x + 1][y] = 2
                        changed = True
                    if y + 1 < len(line) and self.grid[x][y + 1] == 1:
                        new_grid[x][y + 1] = 2
                        changed = True
                    if y - 1 > -1 and self.grid[x][y - 1] == 1:
                        new_grid[x][y - 1] = 2
                        changed = True
        self.grid = new_grid
        return changed

    def has_fresh(self):
        for line in self.grid:
            for item in line:
                if item == 1:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
