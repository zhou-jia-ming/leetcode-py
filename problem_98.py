# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from utils import generate_tree
from utils import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 使用获得中序遍历的结果判断是否为一个升序序列
        my_stack = [root]

        res = []
        while my_stack:
            node = my_stack.pop()
            if isinstance(node, TreeNode):
                if node.right:
                    my_stack.append(node.right)
                my_stack.append(node.val)
                if node.left:
                    my_stack.append(node.left)
            else:
                res.append(node)

        return sorted(res) == res and len(res)==len(set(res))



if __name__ == "__main__":
    s = Solution()
    root = generate_tree([2, 1, 3])
    print(s.isValidBST(root))
    root = generate_tree([1, 1])
    print(s.isValidBST(root))
    #
    root = generate_tree([10, 5, 15, None, None, 6, 20])
    print(s.isValidBST(root))

