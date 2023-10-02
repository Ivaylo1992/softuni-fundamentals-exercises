journal = input().split(', ')

while True:
    command = input()

    if command == 'Craft!':
        break

    operation = command.split(' - ')

    if operation[0] == 'Collect':
        item = operation[1]
        if item in journal:
            continue
        journal.append(item)
    elif operation[0] == 'Drop':
        item = operation[1]
        if item not in journal:
            continue
        journal.remove(item)
    elif operation[0] == 'Combine Items':
        items = operation[1].split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item not in journal:
            continue
        old_item_index = journal.index(old_item)
        journal.insert(old_item_index + 1, new_item)
    elif operation[0] == 'Renew':
        item = operation[1]
        if item not in journal:
            continue
        journal.remove(item)
        journal.append(item)

print(', '.join(journal))
