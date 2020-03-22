# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-22

# 给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：
#
# 目标数组 target 最初为空。
# 按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
# 重复上一步，直到在 nums 和 index 中都没有要读取的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/create-target-array-in-the-given-order
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # 周赛第一题AC。
        target = []
        for i, item in enumerate(nums):
            target.insert(index[i], item)
        return target


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(s.createTargetArray(nums, index))
