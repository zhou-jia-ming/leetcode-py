# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-16


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 判断回文数 一行AC
        return str(x)[::-1] == str(x)


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
