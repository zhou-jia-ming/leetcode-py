# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-27

# 给定一副牌，每张牌上都写着一个整数。
#
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
#
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

from math import gcd
from collections import Counter
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 数字X就是所有vals的最大公约数。
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2


if __name__ == "__main__":
    s = Solution()
    print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
    print(s.hasGroupsSizeX([1]))
