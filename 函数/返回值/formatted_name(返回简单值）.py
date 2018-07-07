# author：K
def get_formatted(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    # 将结果返回函数调用行
    return full_name.title()


musician = get_formatted('jimi', 'hendrix')
print(musician)
