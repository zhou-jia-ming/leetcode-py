# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-05

# 给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：
#
# 如果当前数字为偶数，则将其除以 2 。
#
# 如果当前数字为奇数，则将其加上 1 。
#
# 题目保证你总是可以按上述规则将测试用例变为 1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def numSteps(self, s: str) -> int:
        # 模拟计算。
        i = int('0b{}'.format(s), base=2)
        step = 0
        while i != 1:
            if i % 2 == 0:
                i //= 2
            else:
                i += 1
            step += 1
        return step


if __name__ == '__main__':
    s = Solution()
    print(s.numSteps("1101"))
    print(s.numSteps("10"))
    print(s.numSteps(
        "1111011110000011100000110001011011110010111001010111110001"))
