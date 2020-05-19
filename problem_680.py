# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-19

from typing import *


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 思路，先判断删除的时候是否是回文串。
        # 当不是的时候，两边向中间遍历，遇到第一个不同时，
        # 如果去掉left，中间的部分是回文，或者去掉right中间是回文则，总体是回文，否则不是。
        if s == reversed(s):
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                a = s[left + 1: right + 1]
                b = s[left:right]
                return a == a[::-1] or b == b[::-1]
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("aba"))  # should be True
    print(s.validPalindrome("abar"))  # should be True
