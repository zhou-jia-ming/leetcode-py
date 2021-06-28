from typing import *


class Solution:
    def permutation(self, s: str) -> List[str]:
        chars = list(s)
        chars.sort()
        ans = ["".join(chars)]
        while True:
            reverseIndex = None
            for i in range(len(chars) - 2, -1, -1):
                if chars[i] >= chars[i + 1]:

                    continue
                else:
                    reverseIndex = i
                    break
            if reverseIndex is None:
                break
            for i in range(len(chars) - 1, -1, -1):
                if chars[i] > chars[reverseIndex]:
                    chars[i], chars[reverseIndex] = chars[reverseIndex], chars[
                        i]
                    chars[reverseIndex + 1:] = chars[reverseIndex + 1:][::-1]
                    ans.append("".join(chars))
                    break
            else:
                break
        return ans

s = Solution()
s.permutation("aab")
