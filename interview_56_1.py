# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-28

# 数组中数字出现的次数
# 一个整型数组
# nums
# 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n)，空间复杂度是O(1)。


from typing import *
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a, b = 0, 0

        res = reduce(lambda a, b: a ^ b, nums, 0)
        # 先计算 res = a^b,
        # 找到从右到左第1个1的位数。将数组按照位数不同分成两组，
        # 每组各自按位异或，得到两个数字
        index = 0
        while res & 1 == 0:
            index += 1
            res >>= 1
        for n in nums:
            if n >> index & 1 == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumbers([4, 1, 4, 6]))
