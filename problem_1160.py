# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17


# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
#
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#
# 注意：每次拼写时，chars 中的每个字母都只能用一次。
#
# 返回词汇表 words 中你掌握的所有单词的 长度之和。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            if self.match(chars, word):
                res += len(word)
        return res

    def match(self, chars, word):
        for c in word:
            if c not in chars:
                return False
            chars = chars.replace(c, '', 1)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], 'atach'))
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(s.countCharacters(words, chars))
    words = [
        "dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
        "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
        "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
        "boygirdlggnh",
        "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
        "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
        "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
        "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
        "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl",
        "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
        "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
        "eeilfdaookieawrrbvtnqfzcricvhpiv",
        "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
        "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
        "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
        "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
        "teyygdmmyadppuopvqdodaczob",
        "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
        "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
    chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
    print(s.countCharacters(words, chars))
