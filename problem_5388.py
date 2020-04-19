# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-19

# 重新格式化字符串
# 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
#
# 请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
#
# 请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reformat-the-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def reformat(self, s: str) -> str:
        # 周赛第一题，思路很简单，挨个插入字符。当字符和字母个数相差大于1，不合法
        nums = []
        chars = []
        res = ""
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                chars.append(c)
        if -1 <= len(chars) - len(nums) <= 1:
            if len(chars) == len(nums):
                for i in range(len(nums)):
                    res += nums[i] + chars[i]
            elif len(chars) > len(nums):
                for i in range(len(nums)):
                    res += chars[i] + nums[i]
                res += chars[-1]
            else:
                for i in range(len(chars)):
                    res += nums[i] + chars[i]
                res += nums[-1]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.reformat("xb23"))
