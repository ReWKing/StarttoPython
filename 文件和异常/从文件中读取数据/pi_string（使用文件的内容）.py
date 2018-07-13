# author：K
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    # 删除字符串左右两边的空格
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
