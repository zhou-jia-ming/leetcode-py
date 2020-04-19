# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-19

# 数青蛙
# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。
# 由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。
# 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
#
# 注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。
# 如果没有输出全部五个字母，那么它就不会发出声音。
#
# 如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 周赛第3题，思路：维护一个字符表，表示叫到该字母的青蛙的个数。
        # 每读入一个字符，判断它的前缀字符是否满足>0,到最后一个字符时更新青蛙个数。
        # 由于青蛙叫完可以继续叫，维护一个已经唱完的青蛙个数。
        # 新起一个croak的时候判断是否有唱完的青蛙。遍历结束后判断是否有剩余字符
        num = 0
        chars_bin = {c: 0 for c in "croak"}
        singed = 0
        for c in croakOfFrogs:
            if c == "c":
                chars_bin['c'] += 1
                if singed > 0:
                    singed -= 1
            elif c == "r":
                if chars_bin['c'] > 0:
                    chars_bin['c'] -= 1
                    chars_bin['r'] += 1
                else:
                    return -1
            elif c == "o":
                if chars_bin['r'] > 0:
                    chars_bin['r'] -= 1
                    chars_bin['o'] += 1
                else:
                    return -1
            elif c == "a":
                if chars_bin['o'] > 0:
                    chars_bin['o'] -= 1
                    chars_bin['a'] += 1
                else:
                    return -1
            elif c == "k":
                if chars_bin['a'] > 0:
                    chars_bin['a'] -= 1
                    chars_bin['k'] += 1
                    singed += 1
                    num = max(num, singed)
                else:
                    return -1
            else:
                pass
        if chars_bin['c'] != 0 or chars_bin['r'] != 0 or chars_bin['o'] != 0 or \
                chars_bin['a'] != 0:
            return -1
        if num == 0:
            return -1
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.minNumberOfFrogs("croakcroak"))
    print(s.minNumberOfFrogs("croakcrook"))
