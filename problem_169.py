# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-13

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 常规思路，遍历后统计
        # AC过了，发现最快的人用了排序+取数组中间666
        num_map = defaultdict(lambda: 0)
        length = len(nums)
        for n in nums:
            num_map[n] += 1
            if num_map[n] > length // 2:
                return n


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(s.majorityElement([1]))
