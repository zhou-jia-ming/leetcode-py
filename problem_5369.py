# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-29

# n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。
#
# 每 3 个士兵可以组成一个作战单位，分组规则如下：
#
# 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
# 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，
# 其中  0 <= i < j < k < n
# 请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。
from typing import List


class Solution(object):
    def numTeams(self, rating: List[int]) -> int:

        res = 0
        length = len(rating)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if i < j < k and ((rating[i] < rating[j] < rating[k]) or (
                            rating[i] > rating[j] > rating[k])):
                        res += 1

        return int(res)


if __name__ == "__main__":
    s = Solution()
    print(s.numTeams([1, 2, 3, 4]))
    print(s.numTeams([2, 5, 3, 4, 1]))
