# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 将整数按权重排序
# 我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：

# 如果 x 是偶数，那么 x = x / 2
# 如果 x 是奇数，那么 x = 3 * x + 1
# 比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。
#
# 给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。
#
# 请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。
#
# 注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。

import functools


@functools.lru_cache(None)
def weight(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return \
            sorted([(i, weight(i)) for i in range(lo, hi + 1)],
                   key=lambda a: a[1])[
                k - 1][0]


if __name__ == '__main__':
    s = Solution()
    print(s.getKth(12, 15, 2))
