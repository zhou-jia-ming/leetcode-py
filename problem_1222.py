# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-09

# 在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。
#
# 「黑皇后」在棋盘上的位置分布用整数坐标数组 queens 表示，「白国王」的坐标用数组 king 表示。
#
# 「黑皇后」的行棋规定是：横、直、斜都可以走，步数不受限制，但是，不能越子行棋。
#
# 请你返回可以直接攻击到「白国王」的所有「黑皇后」的坐标（任意顺序）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/queens-that-can-attack-the-king
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # AC中等题， 难度不大，遍历即可
        x, y = king
        res = []
        q_set = set([tuple(_) for _ in queens])
        for q in queens:
            if q[0] == x:
                # if queen's x == king's x
                blocked = False
                i, j = y, q[1]
                if i < j:
                    i += 1
                elif i > j:
                    i -= 1
                while i != j:
                    if (x, i) in q_set:
                        blocked = True
                        break
                    if i < j:
                        i += 1
                    elif i > j:
                        i -= 1
                if not blocked:
                    res.append(q)
            elif q[1] == y:
                # if queen's y == king's y
                blocked = False
                i, j = x, q[0]
                if i < j:
                    i += 1
                elif i > j:
                    i -= 1
                while i != j:
                    if (i, y) in q_set:
                        blocked = True
                        break
                    if i < j:
                        i += 1
                    elif i > j:
                        i -= 1
                if not blocked:
                    res.append(q)
            if (q[0] - q[1]) == (x - y):
                # queen and king in a line which from left top to right bottom
                blocked = False
                ix, iy = x, y
                if ix < q[0]:
                    ix += 1
                    iy += 1
                elif ix>q[0]:
                    ix -= 1
                    iy -= 1
                while ix != q[0]:
                    blocked = False
                    if (ix, iy) in q_set:
                        blocked = True
                        break
                    if ix < q[0]:
                        ix += 1
                        iy += 1
                    elif ix>q[0]:
                        ix -= 1
                        iy -= 1

                if not blocked:
                    res.append(q)
            elif (q[0] + q[1]) == (x + y):
                # queen and king in a line which from right top to right left bottom
                blocked = False
                ix, iy = x, y
                if ix < q[0]:
                    ix += 1
                    iy -= 1
                elif ix>q[0]:
                    ix -= 1
                    iy += 1
                while ix != q[0]:
                    blocked = False
                    if (ix, iy) in q_set:
                        blocked = True
                        break
                    if ix < q[0]:
                        ix += 1
                        iy -= 1
                    elif ix > q[0]:
                        ix -= 1
                        iy += 1

                if not blocked:
                    res.append(q)
        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
    print(s.queensAttacktheKing(
        [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2],
         [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7],
         [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
        , [3, 4]))
