# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21

# 给你一个非负整数num ，请你返回将它变成0所需要的步数。 如果当前数字是偶数，你需要把它除以2 ；否则，减去1 。
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            step += 1
        return step


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(8))
