# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-05

from typing import *


# 旅行终点站
# 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，
# 其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
# 请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
#
# 题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/destination-city
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 根据题意，求终点，终点是不会作为起点的。
        # 思路1，获得所有的城市集合，减去起点城市集合
        # all_city = set()
        # start_city = set()
        # for start, end in paths:
        #     all_city.add(start)
        #     all_city.add(end)
        #     start_city.add(start)
        # return list(all_city - start_city)[0]
        # 思路2，获得所以起点城市和终点城市。终点城市一定包含最终起点。
        # 而非最终终点的终点城市一定在起点城市集合中。
        # starts, ends = set(),set()
        # for s, e in paths:
        #     starts.add(s)
        #     ends.add(e)
        # return list(ends-starts)[0]

        # 思路3，使用一个hash表保存start->end的key-value 对。判断end是否在key中。
        my_dict = dict()
        for s, e in paths:
            my_dict[s] = e
        for s, e in paths:
            if e not in my_dict:
                return e


if __name__ == "__main__":
    s = Solution()
    print(s.destCity(
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
