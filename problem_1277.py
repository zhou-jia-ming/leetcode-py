# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-17

# 飞机座位分配概率
# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
#
# 剩下的乘客将会：
#
# 如果他们自己的座位还空着，就坐到自己的座位上，
#
# 当他们自己的座位被占用时，随机选择其他座位
# 第 n 位乘客坐在自己的座位上的概率是多少？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/airplane-seat-assignment-probability
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import *


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # 如果只有1个乘客，那么坐对的概率是1
        # 其余情况为0.5。推理如下
        # 对于第i个人，i!=1 他坐下以后，第i号座位必然被占，要么被自己坐，要么被别人坐。
        # 来到最后一个人时，有两种可能，一种是n号座位为空，一种不为空。所以是0.5

        # 也可这样推想，如果除了第一个人和最后一个人，
        # 每个上来的人都按照自己的座位坐，如果对方坐错了，就让他找个空座去坐。
        # 最后必然把第一名乘客推向自己的座位和最后一名乘客的座位二选一。
        return 1 if n == 1 else 0.5


if __name__ == "__main__":
    s = Solution()
    print(s.xxx)
