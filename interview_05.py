# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-22

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


if __name__ == "__main__":
    s = Solution()
    print(s.replaceSpace("We are happy."))
