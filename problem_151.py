# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-10

# 翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。


class Solution:
    def reverseWords(self, s: str) -> str:
        # 一行AC
        return " ".join(s.split()[::-1]).strip()


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
