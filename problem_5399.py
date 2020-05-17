# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-17

# 数位成本和为目标值的最大数字
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
#
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。
#
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *
import sys


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        #  周赛第四题，暴力超时，
        # res = 0
        # my_dict = dict()
        # for i, c in enumerate(cost):
        #     val = i + 1
        #     if c in my_dict:
        #         my_dict[c].append(val)
        #     else:
        #         my_dict[c] = [val]
        # for k, v in my_dict.items():
        #     my_dict[k] = max(v)
        #
        # def largest(string, t):
        #     nonlocal res
        #     if t == 0:
        #         res = max(string, res)
        #     if t < 0:
        #         return
        #
        #     for cost, c in my_dict.items():
        #         c = my_dict[cost]
        #         largest(string * 10 + c, t - cost)
        #
        # largest(res, target)
        #
        # return str(res)
        # TODO 这是一道完全背包问题，等我研究研究再写

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
    print(s.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12))
    print(s.largestNumber([70, 84, 55, 63, 74, 44, 27, 76, 34], 659))
