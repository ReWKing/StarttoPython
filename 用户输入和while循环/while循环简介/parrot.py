prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
# 创建了一个变量message用于储存用户输入的值，初始值设置为空字符串""
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


