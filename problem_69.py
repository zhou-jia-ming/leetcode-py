# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-09

# x的平方根

from typing import *


class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        # if x < 1:
        #     return 0
        # if x == 1:
        #     return 1
        # left, right = 0, x
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if mid ** 2 == x:
        #         return mid
        #     elif mid ** 2 > x:
        #         right = mid
        #     else:
        #         left = mid
        #     if mid ** 2 < x < (mid + 1) ** 2:
        #         return mid

        # 数学方法，(a+b)/2 >= sqrt(a+b) ps( a>0,b>0)
        # 每次加上x/r再折半，精度逼近根号x,
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return int(r)

        # 比较取巧的方法，math.floor(math.sqrt(x))或者 int(x**0.5)


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(13))
