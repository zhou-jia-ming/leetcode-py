# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-18

# 重新排列句子中的单词
# 「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :
#
# 句子的首字母大写
# text 中的每个单词都用单个空格分隔。
# 请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，
# 则保留其在原句子中的相对顺序。
#
# 请同样按上述格式返回新的句子。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def arrangeWords(self, text: str) -> str:
        # 周赛第二题，
        # 思路先分词，再按长度排序，拼接，在用capitalize函数处理首字母大写，其余字母小写
        # 排序时间复杂度是N*logN,
        # 使用O(n)的空间，哈希存储每个词的长度，避免排序重复计算长度
        words = text.split(" ")
        lens = {word: len(word) for word in words}
        words.sort(key=lambda a: lens[a])
        return " ".join(words).capitalize()


if __name__ == "__main__":
    s = Solution()
    print(s.arrangeWords("Leetcode is cool"))
