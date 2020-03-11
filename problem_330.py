# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-05
# 给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，
# 使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/patching-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        if n == 0:
            return 0
        miss = 1  # 表示[0,1)被cover
        res = 0
        i = 0
        while miss <= n:
            if (i < len(nums)) and nums[i] <= miss:
                # 如果当前数字小于等于miss, miss增加nums[i]
                miss += nums[i]
                i += 1
            else:
                # 如果当前数字大于miss, miss *2
                miss += miss
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minPatches([1, 3], 6))
