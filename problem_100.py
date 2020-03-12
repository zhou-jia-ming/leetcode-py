# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-12

# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and \
               self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    t1, t2 = TreeNode(1), TreeNode(2)
    print(s.isSameTree(t1, t2))
