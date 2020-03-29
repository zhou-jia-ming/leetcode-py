# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-29
from collections import defaultdict


# 请你实现一个类 UndergroundSystem ，它支持以下 3 种方法：
#
# 1. checkIn(int id, string stationName, int t)
#
# 编号为 id 的乘客在 t 时刻进入地铁站 stationName 。
# 一个乘客在同一时间只能在一个地铁站进入或者离开。
# 2. checkOut(int id, string stationName, int t)
#
# 编号为 id 的乘客在 t 时刻离开地铁站 stationName 。
# 3. getAverageTime(string startStation, string endStation)
#
# 返回从地铁站 startStation 到地铁站 endStation 的平均花费时间。
# 平均时间计算的行程包括当前为止所有从 startStation 直接到达 endStation 的行程。
# 调用 getAverageTime 时，询问的路线至少包含一趟行程。
# 你可以假设所有对 checkIn 和 checkOut 的调用都是符合逻辑的。也就是说，
# 如果一个顾客在 t1 时刻到达某个地铁站，那么他离开的时间 t2 一定满足 t2 > t1 。
# 所有的事件都按时间顺序给出。


class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.times_map = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, check_in_time = self.customer[id]
        self.times_map["{}={}".format(start, stationName)].append(
            t - check_in_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        record = self.times_map["{}={}".format(startStation, endStation)]
        return sum(record) / len(record)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


if __name__ == "__main__":
    obj = UndergroundSystem()
    stationName1 = 'king station'
    stationName2 = 'queue station'
    obj.checkIn(2, stationName1, 2)
    obj.checkOut(2, stationName2, 99)
    print(obj.getAverageTime(stationName1, stationName2))
