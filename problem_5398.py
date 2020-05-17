# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-17

# 统计二叉树中好节点的数目
# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。


from utils import TreeNode, null, generate_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 周赛第三题
        # 思路 深度优先遍历，维护一个最大值向下传递，
        # 递归思路，如果当前节点大于等于最大值则+1，更新最大值，遍历子树，结果相加。
        res = 0
        if not root:
            return res
        res += 1
        if root.left:
            res += self.goodNode(root.left, root.val)
        if root.right:
            res += self.goodNode(root.right, root.val)
        return res

    def goodNode(self, root, maxval):
        res = 0
        if root.val >= maxval:
            res += 1
        if root.left:
            res += self.goodNode(root.left, max(maxval, root.val))
        if root.right:
            res += self.goodNode(root.right, max(maxval, root.val))
        return res


if __name__ == "__main__":
    s = Solution()
    root = generate_tree([3, 3, null, 4, 2])
    print(s.goodNodes(root))
