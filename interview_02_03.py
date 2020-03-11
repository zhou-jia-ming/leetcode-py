# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-middle-node-lcci/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list_node(node):
    s = ""
    while node:
        s += str(node.val)
        if node.next:
            s += '->'
        node = node.next
    if s:
        s += '->NULL'

    print(s)


class Solution(object):
    def deleteNode(self, node: ListNode, n: int) -> None:
        """
               Do not return anything, modify node in-place instead.
        """
        while node.val != n:
            node = node.next

        while node.next:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None


if __name__ == "__main__":
    s = Solution()
    # input_data = [4,5,1,9] and 5
    # output 419

    root = ListNode(4)
    root.next = ListNode(5)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(9)
    s.deleteNode(root, 5)
    print_list_node(root)
