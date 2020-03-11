# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21


# 给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。
#
# 确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/circular-array-loop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution(object):
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)
        for start_p, v in enumerate(nums):
            if v == 0:
                continue
            p = start_p
            visit = [0 for _ in range(length)]
            count = 1
            while p < length:
                if visit[p] == 1:
                    break
                visit[p] = 1
                next_index = (nums[p] + p) % length
                if nums[p] * nums[next_index] < 0:
                    break
                if next_index == start_p and count != 1:
                    return True
                count += 1
                p = next_index

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))
    print(s.circularArrayLoop([1, 1, 2]))
