# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-12

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """ 返回二叉树的层次遍历结果（自底向上)
        """
        if not root:
            return []
        res = []
        cur_node = root

        my_stack = [cur_node]
        while my_stack:
            new_line = [item.val for item in my_stack]
            res.insert(0, new_line)
            new_stack = []
            for node in my_stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            my_stack = new_stack

        return res


if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(3)
    t1.left = TreeNode(9)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)
    print(s.levelOrderBottom)
