# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-26

# 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：
#
# 选择二叉树中 任意 节点和一个方向（左或者右）。
# 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
# 改变前进方向：左变右或者右变左。
# 重复第二步和第三步，直到你在树中无法继续移动。
# 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。
#
# 请你返回给定树中最长 交错路径 的长度。
from utils import TreeNode, generate_tree, null


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(val, node, direct=None):
            self.res = max(self.res, val)
            if not node:
                return
            if direct is None:
                if node.left:
                    dfs(0, node.left, 'left')
                if node.right:
                    dfs(0, node.right, 'right')
            elif direct == 'left':
                dfs(0, node.left, 'left')
                dfs(val + 1, node.right, 'right')
            else:
                dfs(val + 1, node.left, 'left')
                dfs(0, node.right, 'right')

        self.res = 0
        dfs(0, root)
        return self.res


if __name__ == "__main__":
    s = Solution()
    root = generate_tree(
        [1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1, null,
         1])
    print(s.longestZigZag(root))
    root = generate_tree([1, 1, 1, null, 1, null, null, 1, 1, null, 1])
    print(s.longestZigZag(root))
