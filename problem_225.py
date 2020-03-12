# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-12

# 使用两个队列模拟栈


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1.pop(0)
        self.queue2, self.queue1 = self.queue1, self.queue2
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1.pop(0)
        self.queue2.append(x)
        self.queue2, self.queue1 = self.queue1, self.queue2

        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":
    obj = MyStack()
    obj.push(12)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
