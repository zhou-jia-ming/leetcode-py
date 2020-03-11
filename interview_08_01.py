# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-23

# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def waysToStep(self, n: int) -> int:
        # v1 超出内存限制 。。。
        # 分析： 当N很多dp数组也很大，内存占用过多
        # if n < 4:
        #     return {1: 1, 2: 2, 3: 4}.get(n)
        # dp = [int(0) for _ in range(n + 1)]
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 4
        # for i in range(4, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        #
        # return dp[n] % 1000000007

        #  v2 递归法，超时
        # 分析，递归没有记忆，有大量重复计算
        # if n < 4:
        #     return {1: 1, 2: 2, 3: 4}.get(n)
        # else:
        #     return (self.waysToStep(n-1) + self.waysToStep(n-2) + self.waysToStep(n-3)) % 1000000007

        # v3 AC ,使用3个变量保存上次循环的结果，注意每次c取mod不然数字很大的时候超时。
        if n < 4:
            return {1: 1, 2: 2, 3: 4}.get(n)
        a, b, c = 1, 2, 4
        for i in range(4, n + 1):
            a, b, c = b, c, (a + b + c) % 1000000007

        return c % 1000000007


if __name__ == "__main__":
    s = Solution()
    print(s.waysToStep(900750))
