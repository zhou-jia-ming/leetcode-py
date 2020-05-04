# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-05

# 绝对差不超过限制的最长连续子数组

from typing import *


# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，
# 该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
#
# 如果不存在满足条件的子数组，则返回 0 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from heapq import heappush, heappop
        max_heap, min_heap = list(), list()
        res = 0
        l = 0  # l表示滑动窗体的左边
        for r, n in enumerate(nums):
            # 入堆
            heappush(min_heap, [n, r])
            heappush(max_heap, [-n, r])
            # 如果最大值-最小值大于limit,缩减左边。
            while -max_heap[0][0] - min_heap[0][0] > limit:

                while min_heap[0][1] <= l:
                    heappop(min_heap)
                while max_heap[0][1] <= l:
                    heappop(max_heap)
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([8, 2, 4, 7], 4))
