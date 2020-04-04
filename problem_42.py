# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-04

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 解法一，每个柱子左边的最大值和右边的最大值中的较小值减去柱子高度得到本柱子雨水量
        # 缺点，计算太慢，每次取max可以优化
        # res = []
        # for i in range(1, len(height) - 1):
        #     res.append(min(max(height[0:i + 1]), max(height[i:])) - height[i])
        # return sum(res)

        # 解法二 双指针优化一下，两边向中间扫描,
        # 每次比较left_max和right_max,处理那个小的。
        # 比如某left_max=10, right_max=5,对于right所在柱子，
        # left_max>right_max,这意味着即使出现更大的left_max也无关。可以处理。
        if not height:
            return 0
        n = len(height)
        left, right = 0, n - 1
        maxleft, maxright = height[0], height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)

            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([2, 0, 2]))
