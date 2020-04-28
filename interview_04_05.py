# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-29

from typing import *
from utils import TreeNode, generate_tree, null


# 实现一个函数，检查二叉树是否为二叉搜素树。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历，然后检查是否是排序好的。
        # 时间复杂度O(n),空间复杂度O(n),如果使用递归可以优化空间复杂度为O(1)
        def preorder(root):
            if not root:
                return list()
            if not root.left and not root.right:
                return [root.val]
            return preorder(root.left) + [root.val] + preorder(root.right)

        origin_list = preorder(root)
        if len(origin_list) != len(set(origin_list)):
            return False
        return sorted(origin_list) == origin_list


if __name__ == "__main__":
    s = Solution()
    T = generate_tree([5, 1, 4, null, null, 3, 6])
    T = generate_tree([1, 1])
    print(s.isValidBST(T))
