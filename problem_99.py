# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-18

from utils import TreeNode, generate_tree, null, levelOrder, morris_inorder


# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 线索二叉树，使用常数级的辅助空间，中序遍历二叉树
        x = y = pred = None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right

            else:
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val


if __name__ == "__main__":
    s = Solution()
    tree = generate_tree([1, 3, null, null, 2])
    print(s.recoverTree(tree))
    print(morris_inorder(tree))

    tree = generate_tree([3, 1, 4, null, null, 2])
    print(s.recoverTree(tree))
    print(morris_inorder(tree))
