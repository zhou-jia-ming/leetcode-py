# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-30


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        circle = [i for i in range(n)]
        index = m % len(circle) - 1
        # print(circle[index])
        del circle[index]
        while len(circle) > 1:
            index = (index + m - 1) % len(circle)
            # print(circle[index])
            del circle[index]
        return circle[0]


if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(5, 3))
    print(s.lastRemaining(10, 17))
