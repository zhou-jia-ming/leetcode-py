# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-18

from typing import *


# 盛最多水的容器
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 两边向中间扫描，更新面积。
        # 面积等于距离乘以高度的较小值
        # 每次移动较小的高度。
        left, right = 0, len(height) - 1
        area = min(height[left], height[right]) * (right - left)
        while left != right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == "__main__":
    s = Solution()
    print(s.xxx)
