# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-21

# 给你一个整数数组 nums 和一个整数 k。
#
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中「优美子数组」的数目。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]  # 记录奇数的下标
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd) - k):
            # 奇数下标odd[i]和前一个奇数下标odd[i-1]之间有odd[i] - odd[i - 1]个偶数
            # 同样的，往后k个，求odd[i+k]和odd[i+k-1]之间的偶数。
            # 这些偶数选为起点就是一个有k的奇数的连续子数组。有m*n种可能。
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(s.numberOfSubarrays(nums, k))
