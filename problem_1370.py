# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-26

# 给你一个字符串 s ，请你根据下面的算法重新构造字符串：
#
# 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
# 重复步骤 2 ，直到你没法从 s 中选择字符。
# 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
# 重复步骤 5 ，直到你没法从 s 中选择字符。
# 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
# 在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。
#
# 请你返回将 s 中字符重新排序后的 结果字符串 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/increasing-decreasing-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        c = Counter(s)
        my_list = sorted([(k, v) for k, v in c.items()], key=lambda x: x[0])
        res = ""
        trend_up = True
        while my_list:
            if trend_up:
                res += ''.join([item[0] for item in my_list if item[1] > 0])
            else:
                res += ''.join(
                    [item[0] for item in my_list[::-1] if item[1] > 0])
            new_list = []
            for item in my_list:
                if item[1] - 1 > 0:
                    new_list.append((item[0], item[1] - 1))
            my_list = new_list
            trend_up = not trend_up
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.sortString("aaaabbbbcccc"))
