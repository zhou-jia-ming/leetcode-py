# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-26

# 每个元音包含偶数次的最长子字符串
# 给你一个字符串 s ，
# 请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，
# 在子字符串中都恰好出现了偶数次。

# 超时
# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         res = 0
#         for start in range(0, len(s)):
#             for end in range(len(s)-1, start-1, -1):
#                if self.match(s[start:end+1]):
#                    res = max(res, end-start+1)
#         return res
#
#     def match(self, s):
#         s = [c for c in s if c in ('a', 'e', 'i', 'o', 'u')]
#         from collections import Counter
#         c = Counter(s)
#         for k, v in c.items():
#             if v % 2 != 0:
#                 return False
#         return True


class Solution:
    def findTheLongestSubstring_v1(self, s: str) -> int:
        lookup = {0: -1}
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        pntr, buf = 0, 0
        res = 0
        while pntr < len(s):
            if s[pntr] in vowels:
                # buf的每位数 等于当前aeiou的奇偶数量
                buf ^= vowels[s[pntr]]
            if buf in lookup:  # lookup表示一个状态的最早位置。当两个状态相等，更新res
                res = max(res, pntr - lookup[buf])
            else:
                lookup[buf] = pntr
            pntr += 1
        return res

    def findTheLongestSubstring(self, s: str) -> int:
        # 更优雅的写法，每个元音字母用一个在二进制下只含有一个1的数字表示，
        # 当这些元音互相^操作时，如果相同的状态码出现两次，
        # 表示上次出现的位置和现在的位置之间的子数组满足题目条件
        ans, status, n = 0, 0, len(s)
        pos = [-1] * (1 << 5)
        pos[0] = 0

        for i in range(n):
            if s[i] == 'a':
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            if pos[status] != -1:
                ans = max(ans, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))
    print(s.findTheLongestSubstring('id'))
    print(s.findTheLongestSubstring(
        "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"))
