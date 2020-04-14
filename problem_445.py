# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-14

# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utils import ListNode, generate_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        num1 = []
        num2 = []
        while cur1:
            num1.append(str(cur1.val))
            cur1 = cur1.next
        while cur2:
            num2.append(str(cur2.val))
            cur2 = cur2.next
        res = str(int("".join(num1)) + int("".join(num2)))
        ans = cur = ListNode(int(res[0]))
        for c in res[1:]:
            new_node = ListNode(int(c))
            cur.next = new_node
            cur = cur.next
        return ans


if __name__ == "__main__":
    s = Solution()
    l1 = generate_list([7, 2, 4, 3])
    l2 = generate_list([5, 6, 4])
    print(s.addTwoNumbers(l1, l2))
