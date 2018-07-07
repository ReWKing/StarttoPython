# author：K
# 在该函数中,由于animal_type制定了默认值,无需通过实参来指定动物类型,python依然将这个实参视为位置实参,所以应将pet_name放在形参列表开头


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet(pet_name='willie')
