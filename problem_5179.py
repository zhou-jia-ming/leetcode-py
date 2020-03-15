# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15

# Definition for a binary tree node.

# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
#
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#
# 如果有多种构造方法，请你返回任意一种。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balance-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 平衡二叉树 思路如下：
        # 先将所有数值取出，排序后重新构建二叉树
        if not root:
            return None
        self.vals = []
        my_stack = [root]
        while my_stack:
            node = my_stack.pop()
            self.vals.append(node.val)
            if node.left:
                my_stack.append(node.left)
            if node.right:
                my_stack.append(node.right)
        self.vals.sort()
        ans = self.buildTree(self.vals)
        return ans

    def buildTree(self, vals):
        if len(vals) == 1:
            root = TreeNode(vals[0])
        elif len(vals) == 2:
            root = TreeNode(vals[1])
            root.left = TreeNode(vals[0])

        else:
            mid = len(vals) // 2
            root = TreeNode(vals[mid])
            root.left = self.buildTree(vals[0:mid])
            root.right = self.buildTree(vals[mid + 1:])
        return root

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)

    print(s.balanceBST(root))
