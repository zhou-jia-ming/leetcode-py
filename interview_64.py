# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-21

# 求1 + 2 + ... + n ，
# 要求不能使用乘除法、for 、 while 、 if 、 else 、switch、case
# 等关键字及条件判断语句（A?B:C）。


class Solution:
    def sumNums(self, n: int) -> int:
        return int(n == 1) or (self.sumNums(n - 1) + n)


if __name__ == "__main__":
    s = Solution()
    print(s.sumNums(3))
