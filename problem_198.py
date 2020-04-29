# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-29

from typing import *


# 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，
# 能够偷窃到的最高金额。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 使用动态规划，dp[i]表示前0～i的最优结果。
        # 当前最优解等于dp,分两种情况进行比较，
        # 一种是考虑i-1偷了的情况。偷不偷第i个
        # dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
