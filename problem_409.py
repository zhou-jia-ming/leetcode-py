# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-19

# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = Counter(s)
        count = 0
        has_odd = False
        for k, v in char_set.items():
            if v % 2 == 0:
                count += v
            else:
                has_odd = True
                count += v - 1

        return count + int(has_odd)


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
