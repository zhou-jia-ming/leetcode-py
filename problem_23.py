# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-26

# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
from typing import *
from utils import ListNode, generate_list
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 思路1，每次在lists中取出最小值。时间复杂度O(n*k) 执行5252ms
        # k是lists的长度
        # res = None
        # current_node = None
        # while lists:
        #     next_node = None
        #     minval = min([node.val for node in lists if node is not None] + [
        #         float("inf")])
        #
        #     for node in lists:
        #         if node is None:
        #             lists.remove(node)
        #             continue
        #         if node.val == minval:
        #             lists.remove(node)
        #             next_node = node
        #             if node.next is not None:
        #                 lists.append(node.next)
        #             break
        #     if next_node:
        #         if res is None:
        #             res = next_node
        #             current_node = next_node
        #         else:
        #             current_node.next = next_node
        #             current_node = next_node
        # return res

        # 思路2 使用堆,堆的特有属性是插入和删除都是logN,
        # 总体复杂度nlogn 执行用时152ms
        # pq = PriorityQueue()
        # for l in lists:
        #     while l is not None:
        #         pq.put(l.val)
        #         l = l.next
        # res,cur = None,None
        # while not pq.empty():
        #
        #     val = pq.get()
        #     if res is None:
        #         res = ListNode(val)
        #         cur = res
        #     else:
        #         cur.next = ListNode(val)
        #         cur = cur.next
        # return res

        # 思路3 全部取出放入新list,排序后再遍历构建链表
        # 总体复杂度nlogn 执行用时112ms。
        # new_list = []
        # for l in lists:
        #     while l is not None:
        #         new_list.append(l.val)
        #         l = l.next
        # new_list.sort(reverse=True)
        # res, cur = None, None
        # while new_list:
        #
        #     val = new_list.pop()
        #     if res is None:
        #         res = ListNode(val)
        #         cur = res
        #     else:
        #         cur.next = ListNode(val)
        #         cur = cur.next
        # return res
        # 目前排名第一的写法，72ms, 和我的上一个思路一样，
        # 不同在于使用for循环遍历排序后的数组，for比while要快
        a = []
        b = ListNode(0)
        c = b
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
        a.sort()
        for j in a:
            c.next = ListNode(j)
            c = c.next
        return (b.next)


if __name__ == "__main__":
    s = Solution()
    n1 = generate_list([1, 4, 5])
    n2 = generate_list([1, 3, 4])
    n3 = generate_list([2, 6])
    print(s.mergeKLists([n1, n2, n3]))
    print(s.mergeKLists([None]))
    n4 = generate_list([-2, -1, -1, -1])
    print(s.mergeKLists([n4, None]))
