# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-22

# 「快乐前缀」是原字符串中既是前缀（非空）也是后缀（不包括原字符串自身）的字符串。
#
# 给你一个字符串 s，请你返回它的 最长快乐前缀。
#
# 如果不存在满足题意的前缀，则返回一个空字符串。

class Solution:
    def longestPrefix(self, s: str) -> str:
        # 暴力求解
        prefix = s
        suffix = s

        for i in range(len(s) - 1, 0, -1):
            prefix = prefix[1:]
            suffix = suffix[:-1]
            if prefix == suffix:
                return prefix

        return prefix if len(prefix) < len(s) and prefix == suffix else ""


if __name__ == "__main__":
    s = Solution()
    print(s.longestPrefix("level"))
    print(s.longestPrefix("ababab"))
    print(s.longestPrefix("a"))
    print(s.longestPrefix("leetcode"))
