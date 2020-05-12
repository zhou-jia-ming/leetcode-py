# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-12

# 实现一个最小栈，支持top push pop操作，top操作，并在常数时间内检索最小元素。
from typing import *


class MinStack(object):
    # 思路，用list模拟栈，先进后出,每次push的时候，push一个（pushValue,当前最小值)的元组
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(2)
    obj.push(1)
    param_3 = obj.top()
    param_4 = obj.getMin()
    obj.pop()
    print(param_4, param_3)
