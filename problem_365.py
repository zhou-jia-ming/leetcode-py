# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 水壶问题
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
#
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

import math


class Solution(object):
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 贝祖定理,判断是否存在整数a,b令ax+by = z ,z是gcd(a,b)的整数倍
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


if __name__ == "__main__":
    s = Solution()
    # print(s.canMeasureWater(34, 5, 6))
    print(s.canMeasureWater(4, 10, 1))
