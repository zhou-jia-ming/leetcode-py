# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 求交点
# 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
#
# 要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回X值最小的点，X坐标相同则返回Y值最小的点。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int],
                     start2: List[int], end2: List[int]) -> List[float]:
        res = []
        # 求line1的斜率
        k1 = None
        if end1[0] != start1[0]:
            k1 = (end1[1] - start1[1]) / (end1[0] - start1[0])
        k2 = None
        if end2[0] != start2[0]:
            k2 = (end2[1] - start2[1]) / (end2[0] - start2[0])

        # 都垂直与x轴，比较横坐标是否相同，并且纵坐标有重合
        if k1 == k2 == None:
            if start1[0] == start2[0]:
                # 共线
                res = [start1[0],
                       sorted([start1[1], end1[1], start2[1], end2[1]])[1]]
        elif k1 is None:
            # 求line2 y=kx+b 的b2
            b2 = start2[1] - k2 * start2[0]
            # 求line2 与line1 x=start1[0]的交点
            res = [start1[0], start1[0] * k2 + b2]
        elif k2 is None:
            b1 = start1[1] - k1 * start1[0]
            res = [start2[0], start2[0] * k1 + b1]
        else:
            b1 = start1[1] - k1 * start1[0]
            b2 = start2[1] - k2 * start2[0]
            if k1 == k2 and b1 == b2:
                res = [sorted([start1[0], end1[0], start2[0], end2[0]])[1],
                       sorted([start1[1], end1[1], start2[1], end2[1]])[1]]
            elif k1 == k2:
                pass
            else:
                # 联立方程 y = k1*x + b1
                #         y = k2*x + b2
                res = [(b2 - b1) / (k1 - k2), (k2 * b1 - k1 * b2) / (k2 - k1)]

        if not res:
            return res

        if between(res[0], [start1[0], end1[0]]) and \
                between(res[0], [start2[0], end2[0]]) and \
                between(res[1], [start1[1], end1[1]]) and \
                between(res[1], [start2[1], end2[1]]):
            return res
        return []


def between(val, val_range):
    epsilon = 1e-6  # float的误差
    start = min(val_range)
    end = max(val_range)
    if abs(start - val) <= epsilon or abs(end - val) <= epsilon:
        return True
    return start <= val <= end


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([0, 0],
                         [0, 1],
                         [0, 0],
                         [0, -1]))
    print(s.intersection([0, 0],
                         [1, -1],
                         [0, 0],
                         [-1, 1]))
    print(s.intersection([0, 0],
                         [1, 1],
                         [1, 0],
                         [2, 1]))
    print(s.intersection([0, 0],
                         [1, 0],
                         [1, 1],
                         [0, -1]))

    print(s.intersection([12, -55],
                         [59, -60],
                         [4, -55],
                         [81, -62]))
