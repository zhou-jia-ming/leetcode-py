# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-15

# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

# 两个相邻元素间的距离为 1 。
from typing import List
from pprint import pprint
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 解题思想，从零出发，层层外扩，记忆化剪枝
        m, n = len(matrix), len(matrix[0])
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if
                      matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    matrix[ni][nj] = matrix[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return matrix


if __name__ == "__main__":
    s = Solution()
    pprint(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    pprint(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    pprint(s.updateMatrix(
        [[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 1], [1, 1, 1, 1, 0],
         [1, 0, 0, 1, 0]]))
