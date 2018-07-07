# 首先,创建一个待验证用户列表
# 和一个用于储存已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户,知道没有未验证的用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # 函数pop()以每次一个的方式从列表unconfirmed_users末尾删除未验证的用户

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)  # 使用函数append()在confirmed_users中添加元素

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
