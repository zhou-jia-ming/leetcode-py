# coding:utf-8
# Created by: Jiaming
# Created at:

from typing import *
from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        ans = []
        for n in nums:
            rest = deepcopy(nums)
            rest.remove(n)
            for line in self.permute(rest):
                ans.append([n] + line)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
