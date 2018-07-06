#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author：William Gin
'''motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
'''
'''
# 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)
# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)
# 在列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)
# 永久删除元素
del motorcycles[0]
print(motorcycles)
# 删除元素并且该元素可被访问
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
# pop()方法使用
lasted_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + lasted_owned.title() + ".")
# 弹出列表中任意位置的元素
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
'''
motorcycles.remove('ducati')
print(motorcycles)
'''
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")
