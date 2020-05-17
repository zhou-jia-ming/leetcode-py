# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-18

# 收藏清单
# 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。

# 请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *
from functools import reduce


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # 周赛第三题，
        # 思路很简单，首先遍历清单，给每个公司编一个code,
        # code 从1开始，每次遍历到新的公司，code 乘以2。
        # 这样得到的公司遍历在二进制上是1, 10, 100, 1000,... 2^(N-1)
        # 所以每个人的公司清单可以用一个数字来表示就是a^b^c...
        # 当一个清单x和清单y,满足 x!=y 并且 x == (x & y) 说明x是y的子集。
        # 接下来清单两两对比在O(n^2)的时间复杂度内计算得到结果。
        # 空间复杂度是O(n), 公司编号字典 和 公司收藏列表 都是随输入增长线性增长。
        comp_codes = dict()
        i = 1
        comp_list = []
        for line in favoriteCompanies:
            comps = 0  # 记录公司列表各项 异或运算 的结果
            for c in line:
                if c in comp_codes:
                    continue
                else:
                    comp_codes[c] = i
                    i *= 2
                comps ^= comp_codes[c]
            comp_list.append(comps)
        res = []
        for i, line1 in enumerate(comp_list):
            if any([line2 != line1 and line1 == (line2 & line1) for line2 in
                    comp_list]):
                continue
            else:
                res.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.peopleIndexes(
        [["leetcode", "google", "facebook"], ["google", "microsoft"],
         ["google", "facebook"], ["google"], ["amazon"]]))
