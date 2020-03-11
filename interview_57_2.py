# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-07

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 使用公式法直接解第一个数字，如果是整数加入答案，如果小于0退出循环
        res = []
        for n in range(2, target + 1):

            temp = target - n * (n - 1) // 2
            if temp <= 0:
                break
            if temp % n == 0:
                a_1 = temp // n
                res.append([a_1 + i for i in range(n)])
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.findContinuousSequence(20))
