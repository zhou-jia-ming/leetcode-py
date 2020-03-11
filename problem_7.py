# coding:utf-8

# Created at: 2020-01-04
# Created by: Jiaming

# 整数反转
# https://leetcode-cn.com/problems/reverse-integer/

# 执行用时 :32 ms, 在所有 Python3 提交中击败了93.54%的用户
# 内存消耗 :12.6 MB, 在所有 Python3 提交中击败了99.88%的用户

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(-x)[::-1])
        if abs(result) > 2 ** 31:
            return 0
        return result

