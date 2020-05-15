# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-15

from typing import *

# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 思路, 位运算 a^a = 0
        return chr(reduce(lambda a, b: a ^ b, [ord(c) for c in s + t], 0))
        # res = 0
        # for c in s + t:
        #     res ^= ord(c)
        # return chr(res)


if __name__ == "__main__":
    s = Solution()
    print(s.findTheDifference(s="abcd", t="abcde"))
