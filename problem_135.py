# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/candy
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 默写 AC
        length = len(ratings)
        left = [1 for _ in range(length)]
        right = left[:]

        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        res = []
        for i in range(length):
            res.append(max([left[i], right[i]]))
        return sum(res)

        # 贪心法
        # length = len(ratings)
        # left_res = [1 for _ in range(length)]
        # right_res = [1 for _ in range(length)]
        #
        # for i in range(1, length):
        #     # 和左边的人比较， 如果分大于他，多他一个糖
        #     if ratings[i] > ratings[i - 1]:
        #         left_res[i] = left_res[i - 1] + 1
        # for i in range(length - 2, -1, -1):
        #     # 和右边的人比较 如果分大于他，多他一个糖
        #     if ratings[i] > ratings[i + 1]:
        #         right_res[i] = right_res[i+1] + 1
        # res = []
        # for i in range(length):
        #     res.append(max(left_res[i], right_res[i]))
        # return sum(res)


if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 0, 2]))
    print(s.candy([1, 2, 2]))
    print(s.candy([1, 3, 2, 2, 1]))
