# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-29

from typing import *
from utils import TreeNode, generate_tree


# 给定一个非空二叉树，返回其最大路径和。

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 思路，依此计算包含顶点的最大权值，后序遍历，时间复杂度O(N)空间复杂度O(logN)
        ans = float('-inf')

        def max_gain(node):
            nonlocal ans
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 以根节点为最大值。更新最大路径
            ans = max(node.val + left_gain + right_gain, ans)
            # 构建新的最大子路径
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return ans


if __name__ == "__main__":
    s = Solution()
    T = generate_tree([1, 2, 3])
    print(s.maxPathSum(T))
