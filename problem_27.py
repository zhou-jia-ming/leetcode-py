# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-09

# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # AC 双指针。
        if not nums:
            return 0
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] == val:
                p2 += 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
        return p1


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
