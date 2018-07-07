# 将current_number设置成了0
current_number = 0

while current_number < 10:
    # 以步长为1的方式往上数
    current_number += 1
    # 计算current_number与2的求模运算结果
    if current_number % 2 == 0:
        # 如果结果等于0,就执行continue语句,让python忽略余下的代码,并返回循环开头
        continue
    # 如果当前数字不能被2整除,就执行余下的代码
    print(current_number)
