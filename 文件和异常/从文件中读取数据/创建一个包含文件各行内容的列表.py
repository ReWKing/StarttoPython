# author：K
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # 方法readlines（）从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()
# 用for循环来打印lines中的各行
for line in lines:
    print(line.rstrip())
