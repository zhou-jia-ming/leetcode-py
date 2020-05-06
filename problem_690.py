# coding:utf-8
# Created by: Jiaming
# Created at: 2020-05-06


# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
#
# 比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。
# 那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，
# 员工3的数据结构是[3, 5, []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，
# 因此没有体现在员工1的数据结构中。
#
# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/employee-importance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        my_dict = {}
        for e in employees:
            my_dict[e.id] = e.importance, e.subordinates

        my_stack = [id]
        res = 0
        while my_stack:
            res += sum([my_dict[pid][0] for pid in my_stack])
            next_stack = []
            for pid in my_stack:
                if my_dict[pid][1]:
                    next_stack += my_dict[pid][1]
            my_stack = next_stack
        return res


if __name__ == '__main__':
    s = Solution()
    employees = []
    employees.append(Employee(1, 5, [2, 3]))
    employees.append(Employee(2, 3, []))
    employees.append(Employee(3, 3, []))
    print(s.getImportance(employees, 1))
