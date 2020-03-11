# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-04

# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
#
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/create-maximum-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        _max = []
        # 分而治之
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                _max = max(_max, self.merge(self.pick(nums1.copy(), i), self.pick(nums2.copy(), k - i)))
        return _max

    def pick(self, nums, k):
        if not k:
            return []
        _pop = len(nums) - k
        res = []
        while nums:
            num = nums.pop(0)
            while _pop and res and res[-1] < num:
                _pop -= 1
                res.pop()
            res.append(num)
        return res[:k]

    def merge(self, nums1, nums2):
        res = []
        while nums1 and nums2:
            res.append(nums1.pop(0)) if nums1 > nums2 else res.append(nums2.pop(0))
        res.extend(nums2 or nums1)
        return res

        # def pick(nums, k):  # 从nums里取出相对顺序不变的k个数构成的最大数
        #     if not k:
        #         return []
        #     # res是一个stack
        #     res, _pop = [], len(nums) - k  # _pop为允许pop的个数
        #     # 遍历每一个数
        #     while nums:
        #         num = nums.pop(0)
        #         # 如果num小于栈顶，弹出栈顶
        #         while _pop and res and res[-1] < num:
        #             _pop -= 1
        #             res.pop()
        #         res.append(num)
        #     return res[:k]
        #
        # def merge(nums1, nums2):  # 将nums1和nums2各自元素的相对顺序不变合并能产生的最大数
        #     res = []
        #     while nums1 and nums2:
        #         res.append(nums1.pop(0)) if nums1 > nums2 else res.append(nums2.pop(0))
        #     res.extend(nums1 or nums2)
        #     return res
        #
        # _max = []
        # for i in range(k + 1):  # 遍历所有组合方式，取最大的结果
        #     if i <= len(nums1) and k - i <= len(nums2):
        #         _max = max(_max, merge(pick(nums1.copy(), i), pick(nums2.copy(), k - i)))
        # return _max


if __name__ == "__main__":
    s = Solution()
    print(s.maxNumber([3, 4, 6, 5],
                      [9, 1, 2, 5, 8, 3],
                      5))
    print(s.maxNumber([6, 7],
                      [6, 0, 4],
                      5))
