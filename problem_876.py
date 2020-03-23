# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-23

# 链表的中间节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        slow = fast = head
        while fast.next:
            if fast.next:
                fast = fast.next
            else:
                break
            if fast.next:
                fast = fast.next

            else:
                # 链表中有2个中间节点选下一个
                slow = slow.next
                break
            slow = slow.next
        return slow
