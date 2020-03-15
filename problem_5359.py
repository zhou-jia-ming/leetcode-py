# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-15

# 公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 ​​​​​​最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
#
# 团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-performance-of-a-team
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from queue import PriorityQueue


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int],
                       k: int) -> int:
        # 时间复杂度nlogn 排序+最小堆
        items = [(speed[i], efficiency[i]) for i in range(n)]
        items.sort(key=lambda item: item[1], reverse=True)
        all_speed = 0
        ans = 0
        pq = PriorityQueue()  # 保存当前最大速度和
        # items[i][1] 是当前最低效率，遍历一次得到最大值

        for i in range(n):
            all_speed += items[i][0]
            pq.put(items[i][0])
            if pq.qsize() > k:
                low_speed = pq.get()
                all_speed -= low_speed
            val = all_speed * items[i][1]
            if val > ans:
                ans = val
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    print(s.maxPerformance(6,
                           [2, 10, 3, 1, 5, 8],
                           [5, 4, 3, 9, 7, 2],
                           2))
