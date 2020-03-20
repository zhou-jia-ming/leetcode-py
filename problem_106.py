# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 根据一棵树的中序遍历与后序遍历构造二叉树。
from typing import List
from utils import TreeNode, levelOrder


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        left_inorder = inorder[0:index]
        right_inorder = inorder[index + 1:]
        left_post_order = postorder[0:index]
        right_post_order = postorder[index:-1]
        root.left = self.buildTree(left_inorder, left_post_order)
        root.right = self.buildTree(right_inorder, right_post_order)
        return root


if __name__ == "__main__":
    s = Solution()
    res = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(levelOrder(res))
