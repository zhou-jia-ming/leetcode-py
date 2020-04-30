# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-30

from typing import *


# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，
# 那么这个数就是快乐数。
#
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isHappy(self, n: int) -> bool:
        # 模拟过程，集合保存结果，出现1或者循环了，中断模拟。
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = self.next(n)

        return n == 1

    def next(self, n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
