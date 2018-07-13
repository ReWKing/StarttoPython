# author：K
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        # print(line)
        # 消除多余的空白行
        print(line.rstrip())
