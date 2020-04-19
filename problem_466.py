# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-19

# 由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
#
# 如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
# 例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
#
# 现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和
# 两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，
# 其中 S1=[s1,n1] 、S2=[s2,n2] 。
#
# 请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-the-repetitions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 思路，找出循环节,分别计算循环节内的次数+出现循环之前的次数
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0, 0, 0
        recall = dict()
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt, index = s2cnt + 1, 0
            if s1cnt == n1:
                return s2cnt // n2
            if index in recall:
                s1cnt_prime, s2cnt_prime = recall[index]
                pre_loop = (s1cnt_prime, s2cnt_prime)
                in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
                break
            else:
                recall[index] = (s1cnt, s2cnt)

        ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        for i in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans, index = ans + 1, 0
        return ans // n2


if __name__ == "__main__":
    s = Solution()
    s1 = "acb"
    n1 = 4
    s2 = "ab"
    n2 = 2
    print(s.getMaxRepetitions(s1, n1, s1, n2))
