# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-27

# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
#
# 二叉搜索树的定义如下：
#
# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from utils import TreeNode, null, generate_tree
from functools import lru_cache


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return [True, 0,0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            if left[0] and right[0] and ((not node.left) or left[1]<node.val) \
                and ((not node.right) or right[2]>node.val):
                new_sum = node.val + left[3]+right[3]
                new_max = right[1] if node.right else node.val
                new_min = left[2] if node.left else node.val
                self.res = max(self.res, new_sum)
                return [True, new_max, new_min, new_sum]
            return [False, 0,0,0]
        dfs(root)
        return self.res



if __name__ == "__main__":
    s = Solution()
    root = generate_tree(
        [1, 4, 3, 2, 4, 2, 5, null, null, null, null, null, null, 4, 6])
    print(s.maxSumBST(root))
