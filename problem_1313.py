# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 给你一个以行程长度编码压缩的整数列表 nums 。
#
# 考虑每对相邻的两个元素 [a, b] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后有 a 个值为 b 的元素。
#
# 请你返回解压后的列表。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decompress-run-length-encoded-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution(object):
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        for i in range(0, length, 2):
            for j in range(nums[i]):
                res.append(nums[i + 1])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.decompressRLElist([1, 2, 3, 4]))
