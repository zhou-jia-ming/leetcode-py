# coding:utf-8
from typing import *
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int
        if len(points)==1:
            return 1
        ans = 0
        for i, p1 in enumerate(points):
            slope_dict = defaultdict(lambda :0)
            for j, p2 in enumerate(points):
                if (i == j):
                    continue
                if p1[0] == p2[0]:
                    slope_dict["tan90"] += 1
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    slope_dict[slope] += 1
            print(p1, slope_dict)
            ans = max(ans, 1+max(slope_dict.values()))


        return ans


s = Solution()
print(s.maxPoints(points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))





