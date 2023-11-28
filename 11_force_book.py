force_book = {}

while True:
    command = input()
    user_to_change_side = ''
    user_exist = False
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')

        for side, users in force_book.items():
            if force_user in users:
                user_exist = True
                break
        if user_exist:
            continue

        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)

    elif '->' in command:
        force_user, force_side = command.split(' -> ')

        for side, users in force_book.items():
            if force_user in users:
                force_book[side].remove(force_user)

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for side, users in force_book.items():
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
    for user in users:
        print(f'! {user}')