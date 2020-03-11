# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-25

# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/friend-circles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class disjoint(object):
    def __init__(self, length):
        self.array = [-1 for _ in range(length)]

    def find(self, i):
        while self.array[i] != -1:
            i = self.array[i]
        return i

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if (x != y) or (x == -1 and y == -1):
            self.array[x] = y

    def number(self):
        s = set()
        for i, item in enumerate(self.array):
            if i == item or item == -1:
                pass
            else:
                s.add(self.find(i))
        return len(s)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 并查集， 构建连通图，求连通部分的个数。
        if not M:
            return 0
        width = len(M)
        height = len(M[0])
        dsu = disjoint(width * height)
        count = 0
        for i in range(width):
            for j in range(height):
                if M[i][j] == 0:
                    pass
                else:
                    dsu.union(i, j)
                    if i == j:
                        if sum([item for item in M[i]]) + sum([M[i][index] for index in range(width)]) == 2:
                            count += 1
        return dsu.number() + count


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum([[1, 1, 0],
                           [1, 1, 0],
                           [0, 0, 1]]))
