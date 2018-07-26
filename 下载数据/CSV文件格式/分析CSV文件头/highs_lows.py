# author：K
# 导入csv模块
import csv

# 将要使用的文件存储到filename中
filename = 'sitka_weather_07-2014.csv'
# 打开这个文件，并将结果文件存储在f中
with open(filename) as f:
    # 将前面存储的文件作为实参传递给它，创建一个与该文件相关联的阅读器（reader）对象，并将这个阅读器存储在reader中
    reader = csv.reader(f)
    # 调用一次next()，得到文件第一行，其中包含文件头，将返回的值存储在header_row中
    header_row = next(reader)
    print(header_row)
