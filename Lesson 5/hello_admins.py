usernames = ['admin', 'user1', 'user2', 'user3', 'user4', 'user5']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")