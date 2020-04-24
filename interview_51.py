# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-24
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。

from typing import *
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 第一个思路，搜索 O(n^2) 超时
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             res += 1
        # return res
        # 第二个思路，一边遍历数组，一边构建一个有序的数组，
        # 每插入一个，判断插入位置，插入最后没有产生逆序对，
        # 产生逆序对。判断插入位置可以使用二分查找为log(n)，因此时间复杂度O(nlog(n))
        res = 0
        sorted_nums = []
        for n in nums:
            index = bisect.bisect(sorted_nums, n)
            res += len(sorted_nums) - index
            sorted_nums[index:index] = [n]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.reversePairs([7, 5, 6, 4]))
    print(s.reversePairs([1, 3, 2, 3, 1]))
