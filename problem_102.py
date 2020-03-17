# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17

# 二叉树层次遍历
from typing import List

from utils import TreeNode, null, generate_tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 一次AC
        res = []
        if not root:
            return res
        my_stack = [root]
        while my_stack:
            new_stack = []
            new_line = []
            for node in my_stack:
                new_line.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            my_stack = new_stack
            res.append(new_line)
        return res


if __name__ == "__main__":
    s = Solution()
    root = generate_tree([3, 9, 20, null, null, 15, 7])
    print(s.levelOrder(root))
