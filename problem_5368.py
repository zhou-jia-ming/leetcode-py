# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-29

# 在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。
#
# 给你一个整数数组 arr，请你从中找出并返回一个幸运数。
#
# 如果数组中存在多个幸运数，只需返回 最大 的那个。
# 如果数组中不含幸运数，则返回 -1 。
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        lucks = []
        for k, v in c.items():
            if k == v:
                lucks.append(k)
        return max(lucks) if lucks else -1


if __name__ == "__main__":
    s = Solution()
    print(s.findLucky([1, 2, 2, 3, 3, 3]))
