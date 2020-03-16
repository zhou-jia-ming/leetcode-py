# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-16

# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
# 比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/compress-string-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def compressString(self, S: str) -> str:

        if not S:
            return ''

        length = len(S)
        last_c = S[0]
        res = S[0]
        count = 1
        for c in S[1:]:
            if c == last_c:
                count += 1
            else:
                res += '{}{}'.format(count, c)
                count = 1
                last_c = c
        res += '{}'.format(count)
        if length > len(res):
            return res
        return S





if __name__ == "__main__":
    s = Solution()
    print(s.compressString("aabcccccaaa"))

    print(s.compressString("abbccd"))
    print(s.compressString("bb"))
