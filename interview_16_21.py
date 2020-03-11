# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
#
# 返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-swap-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        # v1 超时
        # sum1, sum2 = sum(array1), sum(array2)
        # print(sum1, sum2)
        # diff = sum2 - sum1
        # print(diff)
        #
        # for n in array1:
        #     for m in array2:
        #         if m-n==(diff/2):
        #             return [n, m]
        # return list()

        # v2 执行用时:520ms
        # , 在所有Python3提交中击败了100.00 %的用户内存消耗:33.1MB
        # , 在所有Python3提交中击败了100.00 %的用户

        sum1, sum2 = sum(array1), sum(array2)
        diff = sum2 - sum1
        s1, s2 = set(array1), set(array2)
        for n in s1:
            if (n + (diff / 2)) in s2:
                return [n, int(n + (diff / 2))]
        return list()


if __name__ == "__main__":
    s = Solution()
    print(s.findSwapValues([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
