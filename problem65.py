'''
Description: 
version: 
Author: jiaming
Date: 2021-06-17 22:29:20
LastEditors: jiaming
LastEditTime: 2021-06-17 23:18:41
'''
#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def __init__(self):
        
        self.stats = [
            [2,4,-1,1], # 0初始状态, 遇到数字jump 2，小数点jump 4，字母e jump -1，符号+-, jump 1
            [2,4,-1,-1], # 1符号位 , 遇到数字jump 2，小数点 jump 4，字母ejump -1，符号+- jump -1
            [2,3,6,-1], # 2 整数部分, 遇到数字jump 2，小数点jump3，字母e jump 6，符号+- jump -1
            [5,-1, 6, -1], # 3 左侧有整数的小数点, 遇到数字jump 5，小数点jump -1，字母e jump 6，符号+- jump -1
            [5,-1,-1,-1], # 4 左侧没有整数的小数点, 遇到数字jump 5，小数点 jump -1，字母e jump -1，符号+- jump -1
            [5,-1,6,-1], # 5 小数部分, 遇到数字jump5，小数点jump-1，字母e jump 6，符号+- jump -1
            [8,-1,-1,7], # 6 字符e, 遇到数字 jump 8，小数点 jump -1，字母e jump -1，符号+- jump 7
            [8,-1,-1,-1], # 7 指数符号位, 遇到数字 jump 8，小数点 jump -1，字母e jump -1，符号+- jump -1
            [8,-1,-1,-1], # 8 指数整数部分, 遇到数字jump 8，小数点jump -1，字母e jump -1，符号+- jump -1
        ]
    
        self.good = [2,3,5,8]

    def isNumber(self, s: str) -> bool:
        step = 0
        for c in s:
            if c.isdigit():
                key = 0
            elif c == ".":
                key = 1
            elif c in ("e", "E"):
                key = 2
            elif c in ("+", "-"):
                key = 3
            else:
                step = -1
                break
            if step==-1:
                break
            step = self.stats[step][key]
            if step==-1:
                break

        return step in self.good
# @lc code=end

