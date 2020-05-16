# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-16

from typing import *


# 设计一个 LRU缓存机制， get put操作要在O(1)时间内完成。
# LRU有长度限制，大于容器最大值，则删除最不经常使用的key。


class Node:
    def __init__(self, key="", value=""):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        s = "start->{}".format(self.key)
        cur = self
        while cur.next:
            cur = cur.next
            s += "->{}".format(cur.key)
        return s


class LRUCache:
    # 使用哈希表+双链表实现。哈希使得get为O(1), 链表的增删操作也是O(1)
    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.table = dict()
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.remove_node(node)
            self.insert_node(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            node = Node(key, value)
            self.table[key] = node
            if self.count + 1 <= self.cap:
                self.count += 1
            else:
                # if self.tail.prev.key  in self.table:
                del self.table[self.tail.prev.key]
                self.remove_node(self.tail.prev)

            self.insert_node(node)
        else:
            node = self.table[key]
            node.key, node.value = key, value
            self.remove_node(node)
            self.insert_node(node)
        # print("put", key, value)
        # print(self.head)
        # print(self.table.keys(), end="\n")

    def insert_node(self, node):
        node.prev, node.next = self.head, self.head.next
        # 注意，这里不能使用a,b = c,d这样的形式赋值，会有bug
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev, new = node.prev, node.next
        # 注意，这里不能使用a,b = c,d这样的形式赋值，会有bug
        prev.next = new
        new.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    cache = LRUCache(2)  # 缓存容量

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # 返回 1
    cache.put(3, 3)  # 该操作会使得密钥2作废
    assert cache.get(2) == -1  # 返回 - 1(未找到)
    cache.put(4, 4)  # 该操作会使得密钥1作废
    assert cache.get(1) == -1  # 返回 - 1(未找到)
    assert cache.get(3) == 3  # 返回3
    assert cache.get(4) == 4  # 返回4
