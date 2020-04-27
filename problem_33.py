# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-27

from typing import *
import heapq


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # 左边是有序
                if nums[0] <= target < nums[mid]:
                    # 如果目标在左，二分。
                    right = mid - 1
                else:
                    # 目标在右边，二分。
                    left = mid + 1
            else:
                # 左边不是有序，
                # 右边是有序，判断如果target在右边，二分
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    # target不在右边。
                    right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
