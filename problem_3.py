# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-09


# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针，遍历一次
        max_len = 0
        start = 0
        end = 0
        hash_table = {}
        while end < len(s):
            c = s[end]
            if c not in hash_table:
                hash_table[c] = end
            else:
                start = max(start, hash_table[c] + 1)
                hash_table[c] = end
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("abba"))
