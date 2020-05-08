# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-08

# 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 最大长度向左扩展，保存每次的最大长度。
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        ans = s[0]
        for i in range(1, n):

            odd = s[i - max_len - 1:i + 1]  # 取偶数
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                ans = odd
                max_len += 2
                continue

            even = s[i - max_len:i + 1]
            if i - max_len >= 0 and even == even[::-1]:
                max_len += 1
        return ans

    def longestPalindrome1(self, s: str) -> str:
        #  中心扩展算法，字符串的长度是n,一共有2n-1个中心节点
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        start, end = 0, 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)

            max_len = max(len1, len2)
            if max_len > int(end - start):
                start = i - (max_len - 1) // 2
                end = i + int(max_len / 2)
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        l, r, length = left, right, len(s)
        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abcdefabccbabc"))
