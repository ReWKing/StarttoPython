# author：K
# 首先创建一个列表,其中包含多个'cat'元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# 打印这个列表后,python进入while循环,发现'cat'还在列表中,因此再次进入循环直到'cat'的值不出现在列表中
while 'cat' in pets:
    pets.remove('cat')

print(pets)
