# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-10

# 用栈操作构建数组
# 给你一个目标数组 target 和一个整数 n。每次迭代，需要从  list = {1,2,3..., n} 中依序读取一个数字。
#
# 请使用下述操作来构建目标数组 target ：
#
# Push：从 list 中读取一个新元素， 并将其推入数组中。
# Pop：删除数组中的最后一个元素。
# 如果目标数组构建完成，就停止读取更多元素。
# 题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。
#
# 请返回构建目标数组所用的操作序列。
#
# 题目数据保证答案是唯一的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/build-an-array-with-stack-operations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # 周赛第一题。
        # 思路直接模拟栈的操作
        res = []
        cur = 0
        last_num = None
        l = len(target)
        while cur < l:
            if last_num is None:
                if target[cur] == 1:
                    res.append("Push")
                else:
                    res.append("Push")
                    res.append("Pop")
                last_num = 1
                cur += 1
                continue
            if target[cur] == last_num + 1:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
            cur += 1
            last_num = last_num + 1
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.buildArray([2, 3], 3))
