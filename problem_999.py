# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-26


# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
#
# 车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
#
# 返回车能够在一次移动中捕获到的卒的数量。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/available-captures-for-rook
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 击败95%
        x, y = None, None
        for i in range(8):
            if x is None:
                for j in range(8):
                    if board[i][j] == 'R':
                        x, y = i, j
                        break
        res = 0
        i, j = x, y - 1
        while 0 <= j <= 8 and board[i][j] != "B":
            if board[i][j] == 'p':
                res += 1
                break
            j -= 1

        i, j = x, y + 1
        while 0 <= j < 8 and board[i][j] != "B":
            if board[i][j] == 'p':
                res += 1
                break
            j += 1
        i, j = x + 1, y
        while 0 <= i < 8 and board[i][j] != "B":
            if board[i][j] == 'p':
                res += 1
                break
            i += 1
        i, j = x - 1, y
        while 0 <= i < 8 and board[i][j] != "B":
            if board[i][j] == 'p':
                res += 1
                break
            i -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             ["p", "p", ".", "R", ".", "p", "B", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "B", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."]]))
