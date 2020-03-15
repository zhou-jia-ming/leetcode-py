# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15


# 给定一个二叉树，返回它的中序遍历。
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        my_stack = [root]
        while my_stack:
            node = my_stack.pop()
            if isinstance(node, TreeNode):
                if node.right:
                    my_stack.append(node.right)
                my_stack.append(node.val)
                if node.left:
                    my_stack.append(node.left)
            else:
                res.append(node)
        return res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.inorderTraversal(root))
