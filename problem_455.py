# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，
# 这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，
# 这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/assign-cookies
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心 排序后，从小饼开始和小肚子开始满足
        s = sorted(s)
        g = sorted(g)
        loc = 0
        for n in s:
            if loc > len(g) - 1:
                break
            if g[loc] <= n:
                loc += 1
            else:
                continue
        return loc


if __name__ == "__main__":
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))
    print(s.findContentChildren([1, 2], [1, 2, 3]))
    print(s.findContentChildren([10, 9, 8, 7],
                                [5, 6, 7, 8]))
