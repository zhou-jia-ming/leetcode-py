# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 根据一棵树的前序遍历与中序遍历构造二叉树。
from typing import List
from utils import TreeNode, levelOrder


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        left_inorder = inorder[0:index]
        right_inorder = inorder[index + 1:]
        left_preorder = preorder[1:index + 1]
        right_preorder = preorder[index + 1:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


if __name__ == "__main__":
    s = Solution()
    res = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(levelOrder(res))