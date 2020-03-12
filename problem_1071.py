# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-12

# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
#
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
#  
#
# 示例 1：
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 更优秀的解法，时间复杂度O(n1/n2)
        n1, n2 = len(str1), len(str2)
        if n1 == n2 and str1 != str2:
            return ""
        if n1 == n2 and str1 == str2:
            return str1
        if n1 < n2:
            return self.gcdOfStrings(str2[:n1], str2[n1:])
        if n1 > n2:
            return self.gcdOfStrings(str1[:n2], str1[n2:])
        # 第一版本， AC。
        # max_s = ""
        # p1 = 1
        # len1, len2 = len(str1), len(str2)
        # while p1 <= len1 and p1 <= len2:
        #     if len1 % p1 == 0 and len2 % p1==0:
        #         t1 = int(len1 / p1)
        #         t2 = int(len2 / p1)
        #         if str1[0:p1] != str2[0:p1]:
        #             break
        #         elif t1*str1[0:p1]==str1 and t2*str1[0:p1]==str2:
        #             max_s = str1[0:p1]
        #
        #     p1 += 1
        # return max_s


if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
