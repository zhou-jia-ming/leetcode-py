# coding:utf-8
# Created by: Jiaming
# Created at: 2020-02-28

# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
#
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物。
#
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
#
# 如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
#
# 返回从原点到机器人的最大欧式距离的平方。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/walking-robot-simulation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # AC 水题， 思路就是遍历一遍，取最大
        x, y = 0, 0
        max_distance = 0
        direction = 0
        obstacles_map = dict()
        for item in obstacles:
            obstacles_map[(item[0], item[1])] = True

        for cmd in commands:
            if cmd == -2:
                direction = (direction - 1) % 4
            elif cmd == -1:
                direction = (direction + 1) % 4
            else:

                for i in range(cmd):
                    if direction == 0:
                        next_pos = x, y + 1
                    elif direction == 1:
                        next_pos = x + 1, y
                    elif direction == 2:
                        next_pos = x, y - 1
                    else:
                        next_pos = x - 1, y
                    if next_pos not in obstacles_map:
                        x, y = next_pos
                        max_distance = max(max_distance, x * x + y * y)
        return max_distance


if __name__ == "__main__":
    s = Solution()
    print(s.robotSim([4, -1, 3], []))
    print(s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
