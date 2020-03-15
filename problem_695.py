# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15


# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-area-of-island
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 深度优先搜索 ，时间复杂度（R*C)
        ans = 0
        for i, line in enumerate(grid):
            for j, item in enumerate(line):
                ans = max(ans, self.dfs(grid, i, j))
        return ans

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) \
                or grid[i][j] != 1:
            return 0
        grid[i][j] = 0  # 访问过的元素设置为0，避免重复访问
        ans = 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i + di, j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    print(s.maxAreaOfIsland([[1, 1, 0, 1, 1],
                             [1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1],
                             [1, 1, 0, 1, 1]]))
    print(s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
    print(s.maxAreaOfIsland([[1]]))
    print(s.maxAreaOfIsland([[0, 1]]))
    print(s.maxAreaOfIsland([[1, 1, 0, 0, 0],
                             [1, 1, 0, 0, 0],
                             [0, 0, 0, 1, 1],
                             [0, 0, 0, 1, 1]]))
