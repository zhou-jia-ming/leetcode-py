# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 示例 1:
# s = "abc", t = "ahbgdc"
#
# 返回 true.
#
# 示例 2:
# s = "axc", t = "ahbgdc"
#
# 返回 false.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/is-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # AC 使用了find的结果作为下一次扫描的起点
        for c in s:
            cur_index = t.find(c)
            if cur_index == -1:
                return False
            else:
                t = t[cur_index + 1:]
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("acb", "ahbgdc"))
