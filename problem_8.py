# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-03

# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
# 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
# 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Automaton(object):
    """
    自动机，处理字符串。
    """

    def __init__(self):
        self.tables = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        self.status = "start"
        self.ans = 0
        self.sign = 1

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == "+" or c == "-":
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.status = self.tables[self.status][self.get_col(c)]
        if self.status == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, 2 ** 31 - 1) if self.sign == 1 else min(
                self.ans, -2 ** 31)

        elif self.status == 'signed':
            self.sign == 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        # 直接模拟
        # s = s.strip()
        # if not s:
        #     return 0
        # res = []
        # op = "+"
        # if s[0] in ('-', '+'):
        #     op = s[0]
        # else:
        #     if not s[0].isdigit():
        #         return 0
        #     res.append(s[0])
        #
        # for c in s[1:]:
        #     if c.isdigit():
        #         res.append(c)
        #     else:
        #         break
        # if len(res) == 0:
        #     return 0
        # return min(max(-2 ** 31, int(op + "".join(res))), 2 ** 31 - 1)
        # 优雅的自动机写法
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.ans


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("  -42"))
