# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-24

# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
# 在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
# 给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/the-masseuse-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def massage(self, nums: List[int]) -> int:
        # dfs 超时
        # self.res = 0
        # def dfs(val, last):
        #     self.res = max(self.res, val)
        #     if last+2<len(nums):
        #         dfs(val+nums[last+2], last+2)
        #     if last+3<len(nums):
        #         dfs(val+nums[last+3], last+3)
                
        # dfs(0, -2)
        # return self.res
        # 递推
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(len(nums)):
            if i<2:
                continue
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[len(nums)-1]

                                
if __name__ == '__main__':
    s = Solution()
    print(s.massage([1,2,3,1]))
