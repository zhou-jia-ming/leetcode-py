# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-22

# 你这个学期必须选修 numCourse
# 门课程，记为0到numCourse - 1 。
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程
# 0 ，你需要先完成课程
# 1 ，我们用一个匹配来表示他们：[0, 1]
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？


from typing import *
import collections


class Solution:

    def canFinish(self, nCourses: int, prerequisites: List[List[int]]) -> bool:
        # 思路，dfs +记忆化剪枝
        require_map = collections.defaultdict(list)
        for key, value in prerequisites:
            require_map[key].append(value)

        mem = dict()

        def can_finish(n, path):
            if n in mem:
                return mem[n]
            if n in path:
                return False
            if n not in require_map:
                mem[n] = True
                return True
            else:
                pres = require_map[n]
                for pre in pres:
                    if can_finish(pre, path + [n]):
                        continue
                    else:
                        mem[n] = False
                        return False
                mem[n] = True
                return True

        for i in range(nCourses):
            if not can_finish(i, []):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
