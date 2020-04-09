# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-09

# 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归解法，在n-1得到的组合的中插入()则一定合法，最后去重。
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            parenthesis = self.generateParenthesis(n - 1)
            next_p = []
            for p in parenthesis:
                # 由于对称性，只需插入一半
                for i in range(len(p) // 2 + 1):
                    next_p.append(p[:i] + "()" + p[i:])
            return list(set(next_p))


if __name__ == "__main__":
    s = Solution()
    print(s.xxx)
