# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-05

# 给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 示例 1:
#
# 输入: "bcabc"
# 输出: "abc"
# 示例 2:
#
# 输入: "cbacdcbc"
# 输出: "acdb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicate-letters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """

        :param s:
        :return:
        """
        length = len(s)
        res = [""]
        i = 0
        while i < length:
            c = s[i]
            if c not in res:
                while c < res[-1] and res[-1] in s[i + 1:]:
                    res.pop()
                res.append(c)
            i += 1
        return "".join(res)

        # 最快py解法。 栈+贪心
        # stack = ['0']
        #
        # for i, c in enumerate(s):
        #     if c not in stack:
        #         while c < stack[-1] and stack[-1] in s[i+1:]:
        #             stack.pop()
        #         stack.append(c)
        # return ''.join(stack[1:])


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))
