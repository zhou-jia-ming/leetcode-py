# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-25

# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
# https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/c-bing-cha-ji-by-da-li-wang/

from typing import List


class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        # 空间换时间，新数字加入则更新该数字相邻的两数字的连续长度。
        hash_dict = dict()
        max_length = 0
        for n in nums:
            if n not in hash_dict:
                left = hash_dict.get(n - 1, 0)
                right = hash_dict.get(n + 1, 0)
                cur_length = left + right + 1
                max_length = max(max_length, cur_length)
                hash_dict[n] = cur_length
                hash_dict[n - left] = cur_length
                hash_dict[n + right] = cur_length

        return max_length


if __name__ == "__main__":
    s = Solution()
    # print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([1, 2, 0, 1]))
