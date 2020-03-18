# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-18

# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
#
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
#
# 给出两个矩形，判断它们是否重叠并返回结果。
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 判断矩型重合，
        # 思路：如果矩形不重合，矩形2在矩形2的左侧,右侧，上测，下侧
        # rec1[0]表示最左边横坐标
        # rec1[1]表示最下边纵坐标
        # rec1[2]表示最右边边横坐标
        # rec1[3]表示最上边纵坐标

        # AC
        # if rec1[0] >= rec2[2]:  # 矩形2在左侧
        #     return False
        # if rec1[2] <= rec2[0]:  # 矩形2右侧
        #     return False
        # if rec1[3] <= rec2[1]:  # 矩形2上面
        #     return False
        # if rec1[1] >= rec2[3]:  # 矩形2在下面
        #     return False
        # return True

        # 化简
        return not any([rec1[0] >= rec2[2],
                        rec1[2] <= rec2[0],
                        rec1[3] <= rec2[1],
                        rec1[1] >= rec2[3]])


if __name__ == "__main__":
    s = Solution()
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    print(s.isRectangleOverlap(rec1, rec2))
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    print(s.isRectangleOverlap(rec1, rec2))
    rec1 = [7, 8, 13, 15]
    rec2 = [10, 8, 12, 20]
    print(s.isRectangleOverlap(rec1, rec2))
