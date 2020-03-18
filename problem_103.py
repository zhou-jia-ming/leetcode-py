# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-18

from typing import List
from utils import TreeNode, generate_tree, null

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。
# 即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行


class Solution(object):
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 锯齿形层次遍历
        res = []
        if not root:
            return res

        is_reversed = False
        my_stack = [root]

        while my_stack:
            vals = [node.val for node in my_stack]

            if is_reversed:
                res.append(vals[::-1])
            else:
                res.append(vals)
            new_stack = []
            for node in my_stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            my_stack = new_stack
            is_reversed = not is_reversed
        return res


if __name__ == "__main__":
    s = Solution()
    root = generate_tree([3, 9, 20, null, null, 15, 7])
    print(s.zigzagLevelOrder(root))
