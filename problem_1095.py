# coding:utf-8
# Created by: Jiaming
# Created at:

from typing import *


class MountainArray:
    def __init__(self, data):
        self.data = data

    def get(self, index: int) -> int:
        return self.data[index]

    def length(self) -> int:
        return len(self.data)


class Solution:
    def findInMountainArray(self, target: int,
                            mountain_arr: 'MountainArray') -> int:
        # 思路，先二分找到顶点，先在升序二分找target，找不到在降序找
        left, right = 0, mountain_arr.length() - 1

        while left < right:
            mid = (left + right - 1) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                # 升序
                left = mid + 1
            else:
                right = mid
        top_index = left
        # 在升序种查找
        left, right = 0, top_index
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target:
            return left
        # 在降序中查找
        left, right = top_index, mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target:
            return left
        return -1


if __name__ == "__main__":
    s = Solution()
    # array = [1, 2, 3, 4, 5, 3, 1]
    # m = MountainArray(array)
    # target = 3
    array = [1, 5, 2]
    m = MountainArray(array)
    target = 2
    print(s.findInMountainArray(target, m))
