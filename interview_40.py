# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-20

# 最小的k个数
# 输入整数数组 arr ，找出其中最小的 k 个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
from typing import List
from queue import PriorityQueue


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 思路1优先队列，low first.先存再取
        pq = PriorityQueue()
        for item in arr:
            pq.put(item)
        res = []
        for i in range(k):
            res.append(pq.get())
        return res
        # 思路2， 一行AC 排序后切片
        # return sorted(arr)[:k]



if __name__ == "__main__":
    s = Solution()
    print(s.getLeastNumbers([3, 2, 1], 2))
