# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-17

# https://leetcode-cn.com/problems/consecutive-characters/
from typing import *


# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
#
# 请你返回字符串的能量。

class Solution:
    def maxPower(self, s: str) -> int:
        # 双周赛第1题，维护上一个字符和当前字符累计个数，一次遍历O(n)
        cur, res = 0, 0
        last = None
        for c in s:
            if last is None:
                last = c
                cur = 1
            else:
                if last == c:
                    cur += 1
                else:
                    cur = 1
                    last = c
            res = max(cur, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxPower("leetcode"))
