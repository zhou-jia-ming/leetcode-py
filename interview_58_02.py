# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-21


# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]


if __name__ == "__main__":
    s = Solution()
    print(s.reverseLeftWords("abcdefg", 2))
    assert s.reverseLeftWords("abcdefg", 2) == "cdefgab"
