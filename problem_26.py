# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-09

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # AC 掉， 双指针，快的表示正在遍历的索引，慢指针表示重复开始的索引，
        if not nums:
            return 0
        count, p1, p2 = 1, 0, 1  # p1表示快指针，p2慢指针
        while p2 < len(nums):
            if nums[p1] == nums[p2]:  # 重复，走一步
                p2 += 1
            else:
                nums[count] = nums[p2]
                count += 1  # 不重复，+1,慢指针赋值给新起点。
                p1 = p2
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.removeDuplicates([1, 2, 3]))
    print(s.removeDuplicates([1, 1]))
