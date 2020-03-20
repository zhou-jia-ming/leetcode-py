# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。

from utils import TreeNode, generate_tree, null


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        def dfs(node, path):
            if not node:
                return False

            path = path + [node.val]
            if node.left is None and node.right is None:
                return sum(path) == target
            if node.left and dfs(node.left, path):
                return True
            if node.right and dfs(node.right, path):
                return True
            return False

        return dfs(root, [])


if __name__ == "__main__":
    s = Solution()
    tree = generate_tree([5, 4, 8, 11, null, 13, 4, 7, 2, null, 1])
    print(s.hasPathSum(tree, 22))
    print(s.hasPathSum(None, 0))

