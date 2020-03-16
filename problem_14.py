# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-16


# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 遍历一次。直到出现不同字符break.
        if not strs:
            return ""
        res = ""
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            if len(set([s[i] for s in strs])) == 1:
                res += strs[0][i]
            else:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix([]))
