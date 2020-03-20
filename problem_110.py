# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
from utils import TreeNode, generate_tree, null


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        depth, balance = self.is_balance(root)
        return balance

    def is_balance(self, node):
        if not node:
            return 0, True
        if not node.left and not node.right:
            return 1, True
        if node.left:
            left_depth, left_is_balance = self.is_balance(node.left)
        else:
            left_depth, left_is_balance = 0, True
        if node.right:
            right_depth, right_is_balance = self.is_balance(node.right)
        else:
            right_depth, right_is_balance = 0, True

        return max(left_depth, right_depth) + 1, \
               left_is_balance and right_is_balance and abs(
                   left_depth - right_depth) < 2


if __name__ == "__main__":
    s = Solution()
    tree = generate_tree([3, 9, 20, null, null, 15, 7])
    print(s.isBalanced(tree))
    tree = generate_tree([1, 2, 2, 3, 3, null, null, 4, 4])
    print(s.isBalanced(tree))
    tree = generate_tree([1, null, 2, null, 3])
    print(s.isBalanced(tree))
