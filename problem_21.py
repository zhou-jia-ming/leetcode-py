# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-31

# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
from utils import ListNode, generate_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归解法。每次取一个更小的节点。
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    s = Solution()
    l1 = generate_list([1, 3, 5, 7, 9])
    l2 = generate_list([2, 4, 6, 8, 10])
    # l1 = generate_list([5])
    # l2 = generate_list([1,2,4])
    print(s.mergeTwoLists(l1, l2))
