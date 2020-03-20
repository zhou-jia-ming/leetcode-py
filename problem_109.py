# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
from utils import TreeNode, ListNode, generate_list, levelOrder


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 空列表 return
        if head is None:
            return None
        # 单节点 return
        if head.next is None:
            return TreeNode(head.val)
        # 2个节点 return
        if head.next and head.next.next is None:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root
        # 快慢指针，快指针到终点时，慢指针正好是中点
        prev = fast = slow = head

        while True:
            if fast.next:
                fast = fast.next
            else:
                break
            if fast.next:
                fast = fast.next
            else:
                break
            if slow.next:
                prev = slow
                slow = slow.next
        # 断开链接到中点的link
        prev.next = None
        root = TreeNode(slow.val)
        # 递归生成子树
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


if __name__ == "__main__":
    s = Solution()
    head = generate_list([-10, -3, 0, 5, 9])
    root = s.sortedListToBST(head)
    print(levelOrder(root))
