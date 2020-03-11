# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明: 
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gas-station
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution(object):
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # v1 思路，模拟汽车运行。暴力AC
        # if not gas:
        #     return -1
        # n = len(gas)
        # for i in range(n):
        #     if gas[i] >= cost[i]:
        #         start = pos = i
        #         oil = gas[start] - cost[start]
        #         pos = (pos + 1) % n
        #         while True:
        #             if pos == start:
        #                 return pos
        #             else:
        #
        #                 if oil + gas[pos] - cost[pos] >= 0:
        #                     oil = oil - cost[pos] + gas[pos]
        #                     pos = (pos + 1) % n
        #                 else:
        #                     break
        #
        # return -1

        # v2 O(n)算法，计算环路的总油量和一个当前油量，当前油量记录开始点到当前的油量。
        # 只要总油量>=0 必然可以环一周，。
        total_tank = cur_tank = 0
        starting_station = 0

        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if cur_tank < 0:
                starting_station = i + 1
                cur_tank = 0
        return starting_station if total_tank >= 0 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print(s.canCompleteCircuit([4], [5]))
    print(s.canCompleteCircuit([2], [2]))
    print(s.canCompleteCircuit([5, 1, 2, 3, 4],
                               [4, 4, 1, 5, 1]))
