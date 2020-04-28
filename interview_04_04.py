# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-29

from typing import *
from utils import TreeNode, generate_tree, null


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #  遍历每个节点的深度比较，总复杂度为O(nlogn)
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        # 求二叉树深度Log(n)
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced1(self, root: TreeNode):
        # 更高效的解法，将判断平衡和深度写在一个dfs,向上传递平衡的树的深度，
        # 如果不平衡向上传递-1。时间复杂度O(n*logn)
        def DFS(root):

            if root is None:
                return 0

            ld = DFS(root.left)
            rd = DFS(root.right)

            if ld == -1 or rd == -1 or abs(rd - ld) > 1:
                return -1
            else:
                return 1 + max(ld, rd)

        return DFS(root) >= 0


if __name__ == "__main__":
    s = Solution()
    data = generate_tree([3, 9, 20, null, null, 15, 7])
    print(s.isBalanced(data))
    data = generate_tree([1, 2, 2, 3, 3, null, null, 4, 4])
    print(s.isBalanced1(data))
