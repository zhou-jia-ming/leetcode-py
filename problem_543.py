# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-10

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
# 题目地址: https://leetcode-cn.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            else:
                left_depth = depth(node.left)
                right_depth = depth(node.right)
                self.ans = max(self.ans, left_depth + right_depth + 1)
                return max(left_depth, right_depth) + 1
                # max(, depth(node.right)) + 1

        if not root:
            return 0
        else:
            depth(root)
            return self.ans - 1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(s.diameterOfBinaryTree(root))
