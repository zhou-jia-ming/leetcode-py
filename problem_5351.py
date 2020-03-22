# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
#
# 你挑选 任意 一块披萨。
# Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
# Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
# 重复上述过程直到没有披萨剩下。
# 每一块披萨的大小按顺时针方向由循环数组 slices 表示。
#
# 请你返回你可以获得的披萨大小总和的最大值。
from typing import List

import functools


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        n = len(slices)

        @functools.lru_cache(None)
        def dp(start, end, num):
            if num == 1:
                return max(slices[start: end + 1])

            if end - start + 1 < 2 * num - 1:
                return 0

            # 第一个取end
            ans = slices[end]
            if start == 0 and end == n - 1:
                # 如果起止点是两端, 去掉两端，用掉一个loop
                ans += dp(start + 1, end - 2, num - 1)
            else:
                # 查询剩余最大值
                ans += dp(start, end - 2, num - 1)
            # 和第一个取end-1比较
            ans = max(ans, dp(start, end - 1, num))
            return ans

        return dp(0, n - 1, n // 3)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSizeSlices([8, 9, 8, 6, 1, 1]))
    import time

    #
    t = time.time()
    print(s.maxSizeSlices(
        [6, 3, 1, 2, 6, 2, 4, 3, 10, 4, 1, 4, 6, 5, 5, 3, 4, 7, 6, 5, 8, 7, 3,
         8, 8,
         1, 7, 1, 7, 8]))
    print(time.time() - t)
