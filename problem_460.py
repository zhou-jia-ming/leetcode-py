# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-05


# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。
#
# get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
# put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近 最少使用的键。
# 「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lfu-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        # 频率表每个key对应一个链表
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):

        if node.pre:
            # 重新链接
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            # 如果前一个节点和后一个节点是频率表的首相和末项。删除该频率
            if node.pre is self.freqMap[node.freq][0] and node.nex is \
                    self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)  # 删除旧频率，新建新频率
        self.freqMap[node.freq][-1].pre.insert(node)
        # 更新最小频率
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:  # 如果最小频率比当前频率大1。且最小频率是0，更新最小频率
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        # 取值，更新频率表。
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                # put一个新的key 到keyMap.
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                # 大于缓存数量。
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                # 删除最近 最少使用的键。
                self.keyMap.pop(deleted)
            self.increase(node)



# Your LFUCache object will be instantiated and called as such:

# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
