# author：K
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    # 函数json.dump主要接受两个实参：要存储的数据以及可用于存储数据的文件对象
    json.dump(numbers, f_obj)
