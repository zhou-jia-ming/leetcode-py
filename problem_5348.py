# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 给你两个整数数组
# arr1 ， arr2
# 和一个整数
# d ，请你返回两个数组之间的
# 距离值 。
#
# 「距离值」 定义为符合此描述的元素数目：对于元素
# arr1[i] ，不存在任何元素
# arr2[j]
# 满足 | arr1[i] - arr2[j] | <= d 。

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int],
                             d: int) -> int:
        count = 0
        for item1 in arr1:
            if all([abs(item2-item1)>d for item2 in arr2]):
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
