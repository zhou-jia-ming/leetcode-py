# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15

# 请你设计一个支持下述操作的栈。
#
# 实现自定义栈类 CustomStack ：
#
# CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后则不支持 push 操作。
# void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
# int pop()：返回栈顶的值，或栈为空时返回 -1 。
# void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-a-stack-with-increment-operation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) < self.max_size:
            self.data.append(x)

    def pop(self) -> int:
        if len(self.data) == 0:
            return -1
        return self.data.pop(-1)

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.data):
                self.data[i] += val
            else:
                break


if __name__ == "__main__":

    maxSize = 100
    x = 2
    k = 10
    val = 10
    obj = CustomStack(maxSize)
    obj.push(x)
    param_2 = obj.pop()
    obj.increment(k, val)
