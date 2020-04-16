# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-16

# 给出一个区间的集合，请合并所有重叠的区间。
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 先按照区间的起始排序
        intervals = sorted(intervals, key=lambda a: a[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if prev_end < start:
                # 不重叠
                res.append([start, end])
            else:
                # 合并
                res[-1][0] = min(start, prev_start)
                res[-1][1] = max(end, prev_end)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 4], [4, 5]]))
    print(s.merge([[1, 4], [0, 4]]))
    print(s.merge([[1, 4], [0, 1]]))
    print(s.merge([[1, 4], [0, 0]]))
