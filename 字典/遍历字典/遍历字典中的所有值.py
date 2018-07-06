favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for languages in set(favorite_languages.values()):
    print(languages.title())
