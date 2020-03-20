# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

from typing import List


class Solution(object):
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.dfs([], [], [], n)
        return [["." * q + "Q" + "." * (n - q - 1) for q in data] for data in
                self.result]

    def dfs(self, queens, xy_sum, xy_diff, n):
        y = len(queens)
        if y==n:
            self.result.append(queens)
            return
        for x in range(n):
            if x not in queens and x-y not in xy_diff and x+y not in xy_sum:
                self.dfs(queens + [x], xy_sum+[x+y], xy_diff + [x-y], n)


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
