# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-05

from typing import *

# 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。
# 如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # 遍历数组，记录上一个1的位置和中间0的个数
        zero_count = 0
        last_one = -1
        for i, n in enumerate(nums):
            if n==0:
                zero_count +=1
            else:
                if last_one>0 and zero_count<k:
                    return False
                else:
                    last_one = i
                    zero_count = 0
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
