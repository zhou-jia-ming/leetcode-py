# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-25

# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
#
# 请你返回最终形体的表面积。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        # 击败6% 思路：每个立方条贡献的面积等于底面积+顶面积+四周-和相邻立方重合部分
        area = 0
        for i, line in enumerate(grid):
            for j, item in enumerate(line):
                if item:
                    area += item * 4 + 2
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1],
                                 [i, j - 1]]:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            area -= min(grid[x][y], item)

        return area


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 2], [3, 4]]
    print(s.surfaceArea(grid))
