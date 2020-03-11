# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-11

# 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 双指针从双边向中间扫描，比较两边的值是否为总和的三等分，如果不是，向中间移动
        total = sum(A)
        if total % 3 != 0:
            return False
        target = int(total / 3)
        p1, p2 = 1, len(A) - 2
        r1, r2 = A[0], A[-1]
        if r1 == r2 == target and p2 - p1 > 1:
            return True
        while p1 < p2:
            if r1 != target:
                r1 += A[p1]
                p1 += 1
            if r2 != target:
                r2 += A[p2]
                p2 -= 1
            if r1 == r2 == target and p1<=p2:
                return True
        return False

        # 暴力超时
        # for p1 in range(1, len(A) - 1):
        #     for p2 in range(p1 + 1, len(A)):
        #         r1, r2, r3 = A[0:p1], A[p1:p2], A[p2:]
        #         print(1)
        #         if sum(r1) == sum(r2) == sum(r3):
        #             return True
        # return False


if __name__ == "__main__":
    s = Solution()
    # print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    # print(s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
    # print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    print(s.canThreePartsEqualSum([1, -1, 1, -1]))
    print(s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
