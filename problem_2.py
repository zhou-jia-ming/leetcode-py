# coding:utf-8

# Created at: 2020-01-04
# Created by: Jiaming

# 题目：两数相加
# https://leetcode-cn.com/problems/add-two-numbers/submissions/

# 执行用时 :68 ms, 在所有 Python3 提交中击败了94.10%的用户
# 内存消耗 :12.6 MB, 在所有 Python3 提交中击败了99.59%的用户

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = list(), list()
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        n1, n2 = ''.join(n1), ''.join(n2)
        result = str(int(n1[::-1]) + int(n2[::-1]))
        old_head = None
        while result:
            head = ListNode(int(result[0]))
            head.next = old_head
            old_head = head
            result = result[1:]
        return head
