# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-22

# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution(object):
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, int((n * '9') or 0) + 1))


if __name__ == "__main__":
    s = Solution()
    print(s.printNumbers(2))
