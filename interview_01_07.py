# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-07


# 矩阵旋转90度
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # 行

        # 以x=y为轴翻转
        #  [[1,2,3],
        #   [4,5,6],
        #   [7,8,9]]
        # 变为
        #   [1 4 7]
        #   [2 5 8]
        #   [3 6 9]
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 以中点为轴翻转
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], \
                                                     matrix[i][j]

        # 非原地修改写法，先上下翻转，再以x=y为轴复制对应数字
        # n = len(matrix)
        # r = list(zip(*matrix[::-1]))
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = r[i][j]


if __name__ == "__main__":
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    print(m)
