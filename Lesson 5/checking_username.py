current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user1', 'user2', 'user6', 'user7', 'user8']

for current_user in current_users:
    current_user_lower = current_user.lower()

for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print(f"{new_user} is not avialable.Enter a new username.")
    else:
        print(f"Username {new_user} is available.")