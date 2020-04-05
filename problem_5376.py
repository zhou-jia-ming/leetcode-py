# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-05

# 给你一个数组nums，请你从中抽取一个子序列，满足该子序列的元素之和
# 严格大于未包含在该子序列中的各元素之和。
# 如果存在多个解决方案，只需返回长度最小的子序列。如果仍然有多个解决方案，则
# 返回元素之和最大的子序列。
#
# 与子数组不同的地方在于，「数组的子序列」不强调元素在原数组中的连续性，也就是说，它可以通过从数组中分离一些（也可能不分离）元素得到。
#
# 注意，题目数据保证满足所有约束条件的解决方案是唯一
# 的。同时，返回的答案应当按非递增顺序排列。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # 先排序，然后从大到小取数，知道和大于sum(nums)的一半。
        nums.sort(reverse=True)
        s = sum(nums)
        count = nums[0]
        if count > s - count:
            return nums[0:1]
        for i in range(1, len(nums) + 1):
            count += nums[i]
            if count > s - count:
                break
        return nums[:i + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minSubsequence([4, 3, 10, 9, 8]))
    print(s.minSubsequence([4, 4, 7, 6, 7]))
    print(s.minSubsequence([6]))
    print(s.minSubsequence([10, 2, 5]))
    print(s.minSubsequence([4, 6, 4, 4, 8, 5, 1, 7, 9]))
