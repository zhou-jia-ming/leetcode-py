# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-06

# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场
# ，对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，
# 所以该行程必须从 JFK 出发。
#
# 说明:
#
# 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reconstruct-itinerary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from copy import deepcopy


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 思路，深度优先遍历
        self.res = []
        my_dict = dict()
        for t in tickets:
            if t[0] in my_dict:
                my_dict[t[0]].append(t[1])
            else:
                my_dict[t[0]] = [t[1]]
        self.dfs(deepcopy(my_dict), 'JFK', ['JFK'], len(tickets) + 1)
        return sorted(self.res)[0]

    def dfs(self, rest_tickets, start, paths, max_len):
        if len(paths) == max_len:
            self.res.append(paths)
            return

        if start in rest_tickets:
            for item in sorted(rest_tickets[start]):
                new_rest = deepcopy(rest_tickets)
                new_rest[start] = new_rest[start][::]
                new_rest[start].remove(item)
                res_now = len(self.res)
                self.dfs(new_rest, item, paths + [item], max_len)
                if res_now < len(self.res):
                    break

        else:
            return


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(s.findItinerary(
        [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"],
         ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"], ["AXA", "EZE"],
         ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"],
         ["AUA", "JFK"], ["JFK", "EZE"], ["EZE", "ANU"], ["ADL", "AUA"],
         ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"],
         ["ANU", "TIA"], ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"],
         ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
         ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"],
         ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"], ["ADL", "ANU"],
         ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"],
         ["JFK", "AXA"], ["JFK", "ADL"], ["ADL", "EZE"], ["AXA", "TIA"],
         ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"],
         ["TIA", "AUA"], ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"],
         ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
         ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"],
         ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"], ["TIA", "AUA"],
         ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"],
         ["ANU", "EZE"], ["ADL", "AXA"], ["ANU", "AXA"], ["TIA", "ADL"],
         ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"],
         ["TIA", "JFK"], ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"],
         ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
         ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"],
         ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"], ["ANU", "AUA"],
         ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"],
         ["AXA", "ADL"], ["EZE", "AUA"], ["AXA", "ANU"], ["ADL", "EZE"],
         ["AUA", "EZE"]]))
