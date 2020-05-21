# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-21

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 思路，如果数字全是9，+1变成 1 + n个零，n是数组的长度
        # 否则，从后向前遍历，遇到9，赋值为0，遇到非9，+1并中断循环
        if set(digits) == set([9]):
            return [1] + [0] * len(digits)
        for i in range(-1, -(len(digits)+1), -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([0]))
