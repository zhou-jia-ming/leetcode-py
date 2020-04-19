# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-19

# 给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
# 算法如下
# max_val,max_index = -1,-1
# search_cost = 0
# for i,v in enumerate(arr):
#     if max_val<v:
#         max_val = v
#         max_index=i
#         search_index +=1
# return max_index
# 请你生成一个具有下述属性的数组 arr ：
#
# arr 中有 n 个整数。
# 1 <= arr[i] <= m 其中 (0 <= i < n) 。
# 将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
# 返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def f(self, n, i, k):
        if self.tmp[n][i][k] != -1:
            # 记忆化
            return self.tmp[n][i][k]
        if n == 0 or k == 0 or i == 0:
            # 边界条件。长度为0，或者最长递增序列为0，或者最大值为0，都不存在合法的arr
            self.tmp[n][i][k] = 0
            return 0
        if n == 1 and k == 1:
            # 一个长度且递增1次，说明只有一种情况。不论最大值i等于多少,arr = [i]
            self.tmp[n][i][k] = 1
            return 1
        r = 0
        # 当i出现在末尾，则前面的排列满足长度为n-1,最大升序子序列为k-1, 最大值可以是1～i-1
        for j in range(1, i):
            r += self.f(n - 1, j, k - 1)
            r %= 1000000007
        # 当i出现在非末尾，末尾有i种可能，前面n-1位有f(n-1,i,k)种可能。
        # 所以排列有f(n-1,i,k)*i种可能。
        r += self.f(n - 1, i, k) * i
        r %= 1000000007
        self.tmp[n][i][k] = r
        return r

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # 周赛第四题，这题没做出来。思路是三维dp
        # 数字k这个怎么理解，k是当序列递增时增加的。
        # 比如1，2，3，4。k=4.
        # 比如4，3，2，1。k=1 .可以得出k是最大递增子序列的长度
        # 令dp[n][m][k]等于长度为n,最大值m,最大递增子序列k的个数。

        self.tmp = [[[-1 for t in range(k + 1)] for j in range(m + 1)] for i
                    in range(n + 1)]
        r = 0
        # 累计计算f(n,i,k) # i=1～m
        for i in range(1, m + 1):
            r += self.f(n, i, k)
            r %= 1000000007
        return r


if __name__ == "__main__":
    s = Solution()
    n, m, k = 2, 3, 1
    print(s.numOfArrays(n, m, k))
