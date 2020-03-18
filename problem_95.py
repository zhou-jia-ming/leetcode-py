# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-18

# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

from utils import TreeNode, levelOrder
from typing import List


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate_trees(1, n) if n else []

    def generate_trees(self, start, end):
        # 把每个数字当作根，递归求解左子树和右子树，再合并。
        if start > end:
            return [None, ]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1)
            right_trees = self.generate_trees(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    current_node = TreeNode(i)
                    current_node.left, current_node.right = l, r
                    all_trees.append(current_node)
        return all_trees


if __name__ == "__main__":
    s = Solution()
    trees = s.generateTrees(3)
    for t in trees:
        print(levelOrder(t))
