prompt = "\nTell me something,and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
# 将变量active设置为True，让程序处于初始活动状态，简化了程序
active = True
while active:
    message = input(prompt)
    # 在while循环中，在用户输入后使用一条if语句来检查message的值
    if message == 'quit':
        # 
        active = False
    else:
        print(message)

