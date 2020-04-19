# coding:utf-8
# Created by: Jiaming
# Created at: 2020-04-19

# 点菜展示表
# 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说，
# orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中
# customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而
# foodItemi 是客户点的餐品名称。
# 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，
# 后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，
# 第一列应当填对应的桌号，后面依次填写下单的餐品数量。
#
# 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import *


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 周赛第二题， 思路：先把菜名取出，按照桌子排序订单，然后将订单逐个填入每行。
        res = []
        foods = list(set([o[-1] for o in orders]))
        foods.sort()
        food_dict = {}
        for i, food in enumerate(foods):
            food_dict[food] = i + 1
        res.append(["Table"] + foods)
        orders.sort(key=lambda line: int(line[1]))

        line = [orders[0][1], *[0 for i in range(len(foods))]]
        index = food_dict[orders[0][2]]
        line[index] += 1
        for o in orders[1:]:
            _, table, food = o

            if table != line[0]:
                res.append(line)
                line = [table, *[0 for i in range(len(foods))]]

            index = food_dict[food]
            line[index] += 1
        res.append(line)
        res = [[str(item) for item in line] for line in res]
        return res


if __name__ == "__main__":
    s = Solution()
    orders = [["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"],
              ["Melissa", "2", "Soda"]]

    print(s.displayTable(orders))
