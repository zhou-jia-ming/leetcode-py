# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-26

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
    def findTheLongestSubstring(self, s: str) -> int:
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


if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestSubstring("eleetminicoworoep"))
    print(s.findTheLongestSubstring('id'))
    print(s.findTheLongestSubstring(
        "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"))
