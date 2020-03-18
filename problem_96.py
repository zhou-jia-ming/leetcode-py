# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-18

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？


class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = dict()
        return self.num_trees(1, n) if n else 0

    def num_trees(self, start, end):
        # 递归 + 记忆化。
        if start > end:
            return 1
        if (start, end) in self.memo:
            return self.memo[(start, end)]

        all_nums = 0
        for i in range(start, end + 1):
            left_n = self.num_trees(start, i - 1)
            self.memo[(start, i - 1)] = left_n
            right_n = self.num_trees(i + 1, end)
            self.memo[(i + 1, end)] = right_n
            all_nums += left_n * right_n
        self.memo[(start, end)] = all_nums
        return all_nums


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(1))
    print(s.numTrees(2))
    print(s.numTrees(19))
