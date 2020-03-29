# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-29

# 你现在手里有一份大小为 N x N 的『地图』（网格） grid，
# 上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，
# 你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
#
# 我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 
# 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
#
# 如果我们的地图上只有陆地或者海洋，请返回 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 广度优先遍历，从陆地出发，最远的海洋就是最后一步得到的。记录循环次数。
        import numpy as np
        if len(set(np.array(grid).flatten())) == 1:
            return -1
        else:
            step = 0
            m = len(grid)
            n = len(grid[0])
            queue = []
            for x, line in enumerate(grid):
                for y, item in enumerate(line):
                    if item == 1:
                        queue.append([x, y])

            while len(set(np.array(grid).flatten())) != 1:
                new_queue = []
                for q in queue:
                    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if 0 <= q[0] + dx < m and 0 <= q[1] + dy < n:
                            if grid[q[0] + dx][q[1] + dy] == 0:
                                grid[q[0] + dx][q[1] + dy] = 1
                                new_queue.append([q[0] + dx, q[1] + dy])
                queue = new_queue
                step += 1
            return step


if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
