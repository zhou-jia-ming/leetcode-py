# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-27

# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/wildcard-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def __init__(self):
        self.dp = {}

    def isMatch(self, s: str, p: str) -> bool:
        # 默写v2
        p_len = len(p)
        s_len = len(s)

        if s == p or p == '*':
            return True
        if s == '' or p == '':
            return False

        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]

        return d[p_len][s_len]

    def isMatch_v2(self, s: str, p: str) -> bool:
        # 第二版用了动态规划，
        # 当p[i]是普通字符，D[i][j] = D[i-1][j-1] and p[i]==s[j]
        # 当p[i]是？      D[i][j] = D[i-1][j-1]
        # 当p[i]是星号，   D[i][j] 从True开始后面都是True, 也能匹配空字符串
        s_len = len(s)
        p_len = len(p)

        # base case
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False

        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1

                # find first True if d[p_idx-1] line
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                # * match ''
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                # fill all True in
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == '?':
                # match one , copy result of d[p_idx - 1][s_idx - 1] to d[p_idx][s_idx]
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                # fill
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
        return d[p_len][s_len]

    def isMatch_v1(self, s: str, p: str) -> bool:
        # 第一版， 递归+记忆化
        p = self.remove_duplicate_star(p)
        if (s, p) in self.dp:
            return self.dp[(s, p)]

        elif p == s or p == '*':
            self.dp[(s, p)] = True
        elif p == '' or s == '':
            self.dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            self.dp[(s, p)] = self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            # *可能消耗一个字符 可能一个也不消耗。
            self.dp[(s, p)] = self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        else:
            self.dp[(s, p)] = False
        return self.dp[(s, p)]

    def remove_duplicate_star(self, p):
        while '**' in p:
            p = p.replace('**', '*')
        return p


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("ho", "ho**"))
    print(s.isMatch("aa", "a"))
    print(s.isMatch(
        "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
        "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"))
