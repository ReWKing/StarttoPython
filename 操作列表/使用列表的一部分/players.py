#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author：William Gin
players = ['charles', 'michael', 'florence', 'eli']
# 打印第1-3个元素
print(players[0: 3])
# 打印第2-4个元素
print(players[1: 4])
# 从头打印至第三个元素
print(players[:4])
# 从第三个元素开始打印
print(players[2:])
# 打印最后三个元素
print(players[-3:])
print("-----------------------------------------------")
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
