# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n*logn) 解法
        # 参考第一个算法，在查找循环中使用二分查找
        if not nums:
            return 0
        dp = [nums[0]]
        for n in nums[1:]:
            print('dp=', dp)
            if n > dp[-1]:
                dp.append(n)
            else:
                # 查找
                index = bisect_left(dp, n)
                dp[index] = n
        print(dp)
        return len(dp)

        # O(n^2)复杂度，动态规划，
        # 对于nums[0:i]最长子序列dp[i]应该等于
        # 所有比num[i]小的num[j]中的最大值+1，其中0<=j<i
        # if not nums:
        #     return 0
        #
        # dp = [1 for _ in nums]
        # max_ans = 1
        # for i in range(1, len(nums)):
        #     max_val = 0
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             max_val = max(max_val, dp[j])
        #     dp[i] = max_val + 1
        #     max_ans = max(max_ans, dp[i])
        # return max_ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([3, 1, 2]))
    print(s.lengthOfLIS([2, 2]))
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
