# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 15:23
# @Author  : sunzhen
# @File    : ex5.py
# @Software: PyCharm

# 字符串 打印
# my_name = 'sunzhen'
# my_age = 23
# my_height = 180
# my_weight = 220
# my_eyes = 'black'
# my_teeth = 'white'
# my_hair = 'black'

name = 'sunzhen'
age = 23
height = 180
weight = 220
eyes = 'black'
teeth = 'white'
hair = 'black'

print(f"{name}")
print(f'{height}')
print(f"{weight}")
print(f"{age}")
print(f"{eyes}")
print(f"{teeth}")

total = age + height + weight

print(f"{total}")


# round() 函数 浮点数四舍五入
a = round(1.73333)
print(a)