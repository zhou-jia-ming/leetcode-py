# coding:utf-8
# Created by: Jiaming
# Created at:

from typing import *
from utils import TreeNode, generate_tree


# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        # 思路，中序遍历得到遍历list,在逐个查找 时空复杂度都是O(n)
        # 当然也可以边遍历边判断。
        if not root:
            return None
        my_stack = [root]
        values = []
        while my_stack:
            node = my_stack.pop()
            if isinstance(node, TreeNode):
                if node.right:
                    my_stack.append(node.right)
                my_stack.append((node, node.val))
                if node.left:
                    my_stack.append(node.left)
            else:
                values.append(node)
        for i, node in enumerate(values[:-1]):
            if node[1] == p.val:
                return values[i + 1][0]

        return None


if __name__ == "__main__":
    s = Solution()
    # root = generate_tree([2, 1, 3])
    # p = root
    # print(s.inorderSuccessor(root, p).val)
    root = generate_tree([5, 3, 6, 2, 4, None, None, 1])
    p = root.right
    res = s.inorderSuccessor(root, p)
    if res:
        print(res.val)
