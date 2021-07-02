# coding:utf-8

# 有n个供应商向m个仓库供货
# 要求将仓库都塞满，同时一家供应商尽量向更少的仓库供货

# 输入： suppliers， suppliers[i] 表示第i供应商的产量
#       stores[j], 表示第j个仓库的容量
#       其中sum(suppliers) = sum(stores)
# 输出： res， res

# 思路：由于知道仓库总和等于供应商总和，塞满仓库肯定是没有问题。
# 优化的点就是供应商尽量少跑多家仓库。
# 首先将仓库和供应商放入最大堆中
# 贪心算法, 最大的供应商优先供应最大的库

import heapq


class pair:
    def __init__(self, key, value):
        self.key, self.value = key, value

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def findDistributePlan(self, stores, suppliers):
        stores_heap = [pair(k,v) for k, v  in stores.items()]
        heapq._heapify_max(stores_heap)
        suppliers_heap = [pair(k,v) for k,v in suppliers.items()]
        heapq._heapify_max(suppliers_heap)
        res = dict()
        while len(stores_heap)>0:
            store = heapq._heappop_max(stores_heap)
            supplier = heapq._heappop_max(suppliers_heap)
            if store.value == supplier.value:
                res[supplier.key, store.key] = store.value  # 供应商对应仓库的量
            elif store.value > supplier.value:
                res[supplier.key, store.key] = supplier.value
                store.value -= supplier.value
                stores_heap.append(store)
            else:
                res[supplier.key, store.key] = store.value
                supplier.value -= store.value
                suppliers_heap.append(supplier)
        return res


s = Solution()
suppliers = {"A":100, "B":200,"C":200}
stores = {"store1": 50, "store2": 300, "store3": 150}
result = s.findDistributePlan(stores, suppliers)
print(result)
###########################################
suppliers = {"A": 2, "B": 4, "C": 6, "D": 8, "E": 10}
stores = {"store1": 1, "store2": 3, "store3": 5, "store4": 7, "store5": 14}
result = s.findDistributePlan(stores, suppliers)
print(result)


suppliers = {"A": 2, "B": 4, "C": 6, "D": 8, "E": 10}
stores = {"store1": 1, "store2": 4, "store3": 6, "store4": 8, "store5": 11}
result = s.findDistributePlan(stores, suppliers)
print(result)