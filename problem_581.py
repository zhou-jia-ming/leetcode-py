# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-17

# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度

from typing import *


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 先排序，然后两边向中间遍历，在不一致的地方停下。AC
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        start, end = 0, len(nums) - 1
        while start < end:
            changed = False
            if nums[start] == sorted_nums[start]:
                start += 1
                changed = True
            if nums[end] == sorted_nums[end]:
                end -= 1
                changed = True
            if not changed:
                break
        return end - start + 1


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(s.findUnsortedSubarray([2]))
    print(s.findUnsortedSubarray([1, 3, 2, 2, 2]))
