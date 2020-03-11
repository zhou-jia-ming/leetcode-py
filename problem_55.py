# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution(object):

    def canJump(self, nums: List[int]) -> bool:
        # 贪心法，更优。 从头向前遍历，只要能跳到当前最大终点就更新，如果最后更新到0则可以跳到
        last_pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last_pos:
                last_pos = i
        if last_pos == 0:
            return True
        return False

    def canJump_v1(self, nums: List[int]) -> bool:

        # 遍历法 AC
        # 如果没有 0 一定可以跳到最后
        if 0 not in nums:
            return True

        i = len(nums)
        # 如果只有一个台阶，不用跳就到了。
        if i == 1:
            return True
        # 没有台阶，return False
        if nums[0] == 0:
            return False
        # 对于每个台阶，如果是0，判断前面是否有能跳跃自己的，如果最后是0，只要能跳到自身就可以。
        while i > 0:
            i -= 1
            if nums[i] == 0:
                if i == len(nums) - 1:
                    if any([nums[j] + j >= i for j in range(i)]):
                        continue
                    else:
                        return False
                else:
                    if any([nums[j] + j > i for j in range(i)]):
                        continue
                    else:
                        return False
        return True


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([0]))
    print(Solution().canJump([0, 1]))
    print(Solution().canJump([2, 0, 0]))
