# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-17

# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
#
# 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
#
# 回文串不一定是字典当中的单词。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 思路，如果s的长度是偶数，那么每个字母出现的次数必须是偶数才是回文的排列
        # 如果s的长度是奇数，那么只能有一个字母出现次数是奇数，其余必须是偶数。
        # 总结下来就是，所有的字母出现的次数最多只能有一个奇数。
        my_dict = {}
        for c in s:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1
        count = 0
        for v in my_dict.values():
            if v % 2 == 0:
                continue
            else:
                count += 1
        return count <= 1


if __name__ == "__main__":
    s = Solution()
    print(s.canPermutePalindrome("tactcoa"))
