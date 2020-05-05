# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-05

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 暴力法数组长度为n,k窗体有n-k+1个,时间复杂度O((n-k+1)*k)简化 O(n*k)
        # n = len(nums)
        # return [max(nums[i:i+k]) for i in range(n-k+1)]
        # 思路2 使用双端队列，
        # 存储一个单调栈，每次弹出所有在末尾且小于nums[i]的数字,然后加入num[i]到尾
        # 时间复杂度O(n), 每个元素入队一次，出队一次
        res = []
        queue = []
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] < n:
                queue.pop(-1)
            queue.append(i)
            if i >= k - 1:
                # 清理让窗口长度超过k的队头
                while queue and i - queue[0]+1 > k:
                    queue.pop(0)

                res.append(nums[queue[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
