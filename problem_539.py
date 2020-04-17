# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-17

# 最小时间差
# 给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。


from typing import *


class Solution:
    def convert(self, time_str):
        hour, minute = time_str.split(":")
        return int(hour) * 60 + int(minute)

    def findMinDifference(self, timePoints: List[str]) -> int:
        # 先去重，如果有一样的时间，返回0
        if len(set(timePoints)) < len(timePoints):
            return 0
        # 排序后逐个比较
        timePoints = [item for item in map(self.convert, timePoints)]
        timePoints.sort()
        min_diff = float("inf")
        for index, t in enumerate(timePoints[:-1]):
            min_diff = min(min_diff, timePoints[index + 1] - t)
        # 首尾比较
        min_diff = min(timePoints[0] + 24 * 60 - timePoints[-1], min_diff)
        return min_diff


if __name__ == "__main__":
    s = Solution()
    time_points = ["23:59", "00:00"]
    print(s.findMinDifference(time_points))
