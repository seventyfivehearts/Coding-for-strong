# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 15:35
# @Author  : sunzhen
# @File    : ex6.py
# @Software: PyCharm

# 字符串和文本
# 把双引号或者单引号括在一段本文外面时，Python 就会知道你想要把这些文本变成字符串

types_of_people = 10
x = f"There are{types_of_people} type of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(x)
print(y)

print(f"I side: {x}")
print(f"I also side '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)


