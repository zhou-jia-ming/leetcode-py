# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-19

# 给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。
# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，
# 例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
# 示例 1:
#
# 输入:"-1/2+1/2"
# 输出: "0/1"

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 预处理
        numerator = []
        denominator = []
        operators = []
        num_str = ""
        for c in expression:
            if c not in ["+", "-", "/"]:
                num_str += c
            else:
                if c in ["+", "-"]:

                    if num_str:
                        operators.append(c)
                        denominator.append(int(num_str))
                        num_str = ""
                    else:
                        num_str = c
                else:
                    if len(numerator) == len(denominator):
                        numerator.append(int(num_str))
                    else:
                        denominator.append(int(num_str))
                    num_str = ""
        denominator.append(int(num_str))
        res = [numerator.pop(0), denominator.pop(0)]
        while operators:
            op = operators.pop(0)
            next_num, next_deno = numerator.pop(0), denominator.pop(0)
            lcm = self.least_common_multiple(res[1], next_deno)
            if lcm != next_deno:
                next_num *= lcm / next_deno
                next_deno = lcm
            if res[1] != next_deno:
                res[0] *= lcm / res[1]
                res[1] = lcm
            if op == '+':
                res[0] += next_num
            else:
                res[0] -= next_num
        gcd = self.greatest_common_divisor(res[0], res[1])
        res[0] /= gcd
        res[1] /= gcd
        return "{}/{}".format(int(res[0]), int(res[1]))

    def least_common_multiple(self, x, y):
        # 最小公倍数
        return x * y / self.greatest_common_divisor(x, y)

    def greatest_common_divisor(self, x, y):
        # 辗转相除 求最大公约数
        while y != 0:
            x, y = y, x % y
        return x


if __name__ == "__main__":
    s = Solution()
    print(s.fractionAddition("-1/2+1/2"))
    print(s.fractionAddition("-1/2+1/2+1/3"))
    print(s.fractionAddition("1/3-1/2"))
