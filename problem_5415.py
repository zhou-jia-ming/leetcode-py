# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-18

# 墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。
#
# 投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。
#
# 请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        # 周赛第四题，
        # 这是一道计算几何题目，思路是飞镖两两取点，以两点直线做弦，求圆心，
        # 然后得到的圆心与每个点求距离得到能容纳的飞镖，在时间O(n^3)内得到最大的数。
        # 先mark一下，研究研究再写。
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.numPoints, [[-2, 0], [2, 0], [0, 2], [0, -2]], 2)
