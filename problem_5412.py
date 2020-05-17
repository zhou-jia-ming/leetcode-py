# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-18

# 在既定时间做作业的学生人数

# 给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。
# 已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。

# 请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，
# 返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int],
                    queryTime: int) -> int:
        # 周赛第一题 遍历一次 O(n) 思路，queryTime在[start, end] 区间+1
        length = len(startTime)
        res = 0
        for i in range(length):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.busyStudent([1, 2, 3], [3, 2, 7], 4))
