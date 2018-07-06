#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author：William Gin

# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
'''
for循环命名：
for cat in cats:
for dog in dogs:
for item in item_list:
'''
# 在for循环中执行更多操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see you next trick," + magician.title() + ".\n")

print("Thank you,everyone.That was a great magic show!")
