# author：K
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry', 'hamster')
# 1.调用函数多次
describe_pet('dog', 'willie')
# 2.位置实参的顺序很重要
describe_pet('harry', 'hamster')
