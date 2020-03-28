# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-28

# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        num = reversed(str(num))
        for i, c in enumerate(num):
            if i == 0:
                one, five, ten = "I", "V", "X"

            elif i == 1:
                one, five, ten = "X", "L", "C"
            elif i == 2:
                one, five, ten = "C", "D", "M"
            else:
                one, five, ten = "M", None, None
            c = int(c)
            if c == 0:
                pass
            elif 1 <= c <= 3:
                res.append(one * c)
            elif c == 4:
                res.append(one + five)
            elif c == 5:
                res.append(five)
            elif 6<=c<=8:
                res.append(five + one * (c-5))
            else:
                res.append(one * (10 - c) + ten)
        return "".join(reversed(res))


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(58))
