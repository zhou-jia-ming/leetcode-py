# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-02


# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/game-of-life
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 思路，更新会互相影响，要设定一个中间状态，最后再处理一下。
        m = len(board)
        n = len(board[0])
        for i, line in enumerate(board):
            for j, item in enumerate(line):
                if item == 0:
                    # 死细胞
                    count = 0
                    for dx, dy in [(-1, -1),
                                   (-1, 0),
                                   (-1, 1),
                                   (0, 1),
                                   (0, -1),
                                   (1, -1),
                                   (1, 0),
                                   (1, 1)]:
                        if 0 <= i + dx < m and 0 <= j + dy < n:
                            if board[i + dx][j + dy] in (1, 3):
                                count += 1
                    # 死细胞周围正好3个细胞，复活
                    if count == 3:
                        # 先设为2，等下再变回1
                        board[i][j] = 2
                if item == 1:
                    # 活细胞
                    count = 0
                    for dx, dy in [(-1, -1),
                                   (-1, 0),
                                   (-1, 1),
                                   (0, 1),
                                   (0, -1),
                                   (1, -1),
                                   (1, 0),
                                   (1, 1)]:
                        if 0 <= i + dx < m and 0 <= j + dy < n:
                            if board[i + dx][j + dy] in (1, 3):
                                count += 1
                    # 活细胞周围少于2，死亡
                    if count < 2:
                        # 先设为3，等下设置为0
                        board[i][j] = 3
                    elif count > 3:
                        board[i][j] = 3
                    else:
                        pass
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        return


if __name__ == '__main__':
    s = Solution()
    s.gameOfLife([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ])
