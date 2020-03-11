# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-09

# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/odd-even-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        cur = self
        s = ''
        while cur:
            s += "{}->".format(cur.val)
            cur = cur.next
        s += 'NULL'
        return s


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        # 难度中等，一次遍历.准备两个pointer,一个表示奇head,一个是偶head.
        if not head:
            return
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next  # A->C
            odd = odd.next  # A=C
            even.next = odd.next  # B->D
            even = even.next  # B=D

        odd.next = even_head

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    print(s.oddEvenList(head))
