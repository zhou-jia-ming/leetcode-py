# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:
        # 默写 AC
        jump_time = 0
        start, end = 0, 0

        while end < len(nums) - 1:
            jump_time += 1
            far = max([nums[i] + i for i in range(start, end + 1)])
            start, end = end + 1, far
        return jump_time

        # 贪心算法 尽可能跳的更远

        # jump_time = 0
        # start = 0
        # end = 0
        # while end < len(nums) - 1:
        #     jump_time += 1
        #     far = max([nums[i] + i for i in range(start, end + 1)])
        #     start = end + 1
        #     end = far
        # return jump_time


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
