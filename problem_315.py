# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Node(object):
    def __init__(self, val):
        self.count = 0
        self.left = None
        self.right = None
        self.val = val


class Solution(object):
    def countSmaller(self, nums: List[int]) -> List[int]:
        # v1 超时
        # if len(nums)==0:
        #     return list()
        # counts = []
        # i = 0
        # while i<len(nums)-1:
        #     count = 0
        #     for n in nums[i+1:]:
        #         if n< nums[i]:
        #             count += 1
        #     i += 1
        #     counts.append(count)
        # counts.append(0)
        # return counts

        # 二叉搜索树
        length = len(nums)
        root = None
        res = [0 for _ in nums]
        for i in reversed(range(length)):
            root = self.insertNode(root, nums[i], res, i)

        return res

    def insertNode(self, root, val, res, res_index):
        if root is None:
            root = Node(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, val, res, res_index)
        elif val > root.val:
            res[res_index] += root.count + 1
            root.right = self.insertNode(root.right, val, res, res_index)
        return root


if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))
    print(s.countSmaller([1, 1, 1, 1]))
    print(s.countSmaller([0, 1, 2]))
