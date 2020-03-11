# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21


# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution(object):
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])


if __name__ == "__main__":
    s = Solution()
    print(s.findNumbers([12, 345, 2, 6, 7896]))
