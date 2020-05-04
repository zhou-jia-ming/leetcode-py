# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-05

# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
#
# 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # 维护全排序的前k个，每次取一行，上一排的排列和与当前行做分配，每次取前k个进行优化。
        # 时间复杂度。O(m*n*k)
        res = [0]  # res表示一个排列的和
        for row in mat:
            # res是取i个数字的前k个排列的和。
            res = sorted([x+r for x in row for r in res])[:k]
        return res[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.xxx)
