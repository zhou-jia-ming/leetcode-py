# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-17

# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] == target:
            return start
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 0))
    print(s.search([5], 5))
