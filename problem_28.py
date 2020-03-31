# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-31


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        nxt = kmp_next(needle)
        target_index = 0
        pattern_index = 0
        while target_index < len(haystack):

            if haystack[target_index] == needle[pattern_index]:  # 相等扩展1位
                target_index += 1
                pattern_index += 1
            elif pattern_index:
                pattern_index = nxt[pattern_index - 1]  # 不等，回退模式串。
            else:
                target_index += 1
            if pattern_index == len(needle):  # 匹配到最后一位返回索引
                return target_index - pattern_index
        return -1


def kmp_next(p):
    next_array = [0]  # 空字符串最长公共前缀是0
    x = 1
    now = 0
    while x < len(p):

        if p[now] == p[x]:  # 相等，扩展一位
            now += 1
            x += 1
            next_array.append(now)  # now是最长公共前后缀长度
        elif now:
            # 不等 回退[-1]的值，说白了，前面的next数组可用，不用回退到0就可以继续比较。
            now = next_array[now - 1]
        else:
            # now=0且不想等 最长公共前后缀为0
            next_array.append(0)
            x += 1
    return next_array


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))
    # print(s.xxx)
