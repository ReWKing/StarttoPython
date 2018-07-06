'''
# 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
'''
'''
# 遍历元组的所有值
dimensions = (200, 50)
for dimensions in dimensions:
    print(dimensions)
'''
# 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimensions in dimensions:
    print(dimensions)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimensions in dimensions:
    print(dimensions)
