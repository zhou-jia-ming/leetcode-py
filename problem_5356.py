# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15

# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
#
# 幸运数是指矩阵中满足同时下列两个条件的元素：
#
# 在同一行的所有元素中最小
# 在同一列的所有元素中最大
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # 双100% 暴力枚举
        m = len(matrix)
        n = len(matrix[0])
        min_lines = set()
        max_cols = set()
        for i in range(m):
            min_lines.add(min(matrix[i]))
        for i in range(n):
            max_cols.add(max([matrix[j][i] for j in range(m)]))

        return list(min_lines & max_cols)


if __name__ == "__main__":
    s = Solution()
    print(s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
