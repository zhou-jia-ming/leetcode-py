# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17

# 我们从二叉树的根节点 root 开始进行深度优先搜索。
#
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
#
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
#
# 给出遍历输出 S，还原树并返回其根节点 root。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from utils import TreeNode, levelOrder


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # AC 思路如下：
        # 保存每一层的节点，由于是深度遍历，父节点必定是上一层的最后一个。
        # 依次遍历得到深度和数值，
        # 根据深度得到父节点，如果父节点的左节点为空，赋值给左节点，否则给右节点
        if not S:
            return None

        root = None
        stacks = []
        depth = 0
        num_str = ''
        for c in S:
            if c == '-':
                if num_str:
                    new_node = TreeNode(int(num_str))
                    if not stacks:
                        root = new_node
                        stacks.append([root])
                    else:
                        father_node = stacks[depth - 1][-1]
                        if father_node.left is None:
                            father_node.left = new_node
                        else:
                            father_node.right = new_node
                        if len(stacks) < depth + 1:
                            stacks.append([new_node])
                        else:
                            stacks[depth].append(new_node)
                    depth = 1
                    num_str = ''
                else:
                    depth += 1

            else:
                num_str += c
        new_node = TreeNode(int(num_str))
        if root is None:
            return new_node
        father_node = stacks[depth - 1][-1]
        if father_node.left is None:
            father_node.left = new_node
        else:
            father_node.right = new_node
        return root


if __name__ == "__main__":
    s = Solution()
    input_s = "1-2--3--4-5--6--7"
    print(levelOrder(s.recoverFromPreorder(input_s)))
    root = s.recoverFromPreorder("1-401--349---90--88")
    print(levelOrder(root))
    root = s.recoverFromPreorder("1-2--3---4-5--6---7")
    print(levelOrder(root))
    root = s.recoverFromPreorder("3")
    print(levelOrder(root))
    root = s.recoverFromPreorder("10-7--8")
    print(levelOrder(root))
