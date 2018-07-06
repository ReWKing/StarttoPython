favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
