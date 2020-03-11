# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-28

# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
#
# 顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
#
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
#
# 注意，一开始你手头没有任何零钱。
#
# 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lemonade-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # AC 水题 ，贪婪算法。先尽可能把大额的零钱找出去
        my_money = defaultdict(lambda: 0)

        for bill in bills:
            if bill == 5:
                my_money[5] += 1
            if bill == 10:
                if my_money[5] == 0:
                    return False
                else:
                    my_money[5] -= 1
                    my_money[10] += 1
            if bill == 20:
                if my_money[10] > 0 and my_money[5] > 0:
                    my_money[20] += 1
                    my_money[10] -= 1
                    my_money[5] -= 1
                elif my_money[5] > 2:
                    my_money[20] += 1
                    my_money[5] -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5, 5, 5, 10, 20]))
    print(s.lemonadeChange([10, 20]))
