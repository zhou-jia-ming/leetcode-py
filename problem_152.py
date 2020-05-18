# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-18

from typing import *


from functools import lru_cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 思路1，取两个数做为起点和终点，两两求累计乘积，超时
        # @lru_cache(None)
        # def count(i,j):
        #     if i==j:
        #         return nums[i]
        #     if i+1==j:
        #         return nums[i]*nums[j]
        #     return count(i,j-1)*nums[j]

        # l = len(nums)
        # ans = float("-inf")
        # for i in range(l):
        #     for j in range(i,l):
        #         ans = max(ans,count(i,j))
        # return ans
        # 思路2 每个子数组都有一个前缀和后缀，
        # 以当前索引为起点或终点，可以向前或者向后扩展直到0为止。
        # 统计每个前缀后缀乘积的最大值 就是结果
        prefix, suffix, res = 0, 0, -float('inf')
        for i in range(len(nums)):
            # 如果前缀乘积是0，取当前数，否则相*
            prefix = nums[i] if not prefix else nums[i]*prefix
            # 如果后缀乘积是0，取当前数，否则相*
            suffix = nums[-i - 1] if not suffix else nums[-i - 1]*suffix
            # prefix是nums[i]的不含0的前缀乘积
            # suffix是nums[i]的不含0的后缀乘积， 更新最大乘积
            res = max(res, prefix, suffix)
        return res





if __name__ == "__main__":
    s = Solution()
    print(s.xxx)
