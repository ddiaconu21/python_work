users = {
    'ppr': {
        'first': 'parparel',
        'last': 'parpicel',
        'nickname': 'haiosel',
    },

    'ccr': {
        'first': 'capy',
        'last': 'cipcirel',
        'nickname': 'checulet',
    },
    'truchi': {
        'first': 'trucu',
        'last': 'lucu',
        'nickname': 'trucululu'
    }
}

for username, user_info in users.items():
    print(f"\nYour username is: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['nickname']

    print(f"Your full name is: {full_name.title()}")
    print(f"Your nickname is: {location.title()}")

