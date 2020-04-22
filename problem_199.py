# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-22

# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
from typing import *
from utils import TreeNode, generate_tree, null


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 思路1，层次遍历，取最右
        res = []
        if not root:
            return res
        cur_level = [root]
        while cur_level:
            next_level = []
            res.append(cur_level[-1].val)
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return res


if __name__ == "__main__":
    s = Solution()
    root = generate_tree([1, 2, 3, null, 5, null, 4])
    print(s.rightSideView(root))
