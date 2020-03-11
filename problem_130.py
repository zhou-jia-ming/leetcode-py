# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-25


# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
from typing import List


class Solution(object):
    def solve(self, board: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
        """
        # 思路， 先用DFS把边界的O和与其相邻的O标记为-，然后把剩下的O替换为X，再把-转换为O。
        if not board:
            return

        def dfs(x, y):
            if board[x][y] == 'O':
                board[x][y] = '-'
                if 0 <= x - 1 < len(board):
                    dfs(x - 1, y)
                if 0 <= x + 1 < len(board):
                    dfs(x + 1, y)
                if 0 <= y - 1 < len(board[0]):
                    dfs(x, y - 1)
                if 0 <= y + 1 < len(board[0]):
                    dfs(x, y + 1)

            else:
                return

        length_x = len(board)
        length_y = len(board[0])
        for x in range(length_x):
            dfs(x, 0)
            dfs(x, length_y - 1)
        for y in range(length_y):
            dfs(0, y)
            dfs(length_x - 1, y)

        for x, line in enumerate(board):
            for y, item in enumerate(line):
                if item == 'O':
                    board[x][y] = 'X'

        for x, line in enumerate(board):
            for y, item in enumerate(line):
                if item == '-':
                    board[x][y] = 'O'


if __name__ == "__main__":
    s = Solution()
    print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
    print(s.solve(
        [["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"],
         ["O", "X", "O", "X"]]))
