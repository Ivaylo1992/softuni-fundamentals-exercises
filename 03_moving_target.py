targets_list = list(map(int, input().split()))

while True:

    command = input()

    if command == 'End':
        break

    action = command.split()
    type_of_action = action[0]

    if type_of_action == 'Shoot':
        index, power = int(action[1]), int(action[2])

        if index > len(targets_list) or index < 0:
            continue

        targets_list[index] -= power

        if targets_list[index] <= 0:
            targets_list.pop(index)

    elif type_of_action == 'Add':
        index, value = int(action[1]), int(action[2])

        if index not in range(len(targets_list) + 1):
            print("Invalid placement!")
            continue

        targets_list.insert(index, value)

    elif type_of_action == 'Strike':
        index, radius = int(action[1]), int(action[2])
        if index - radius not in range(len(targets_list)+1) \
                or index + radius not in range(len(targets_list)+1):
            print("Strike missed!")
            continue
        del targets_list[index - radius: index + radius + 1]

string_list = [str(num) for num in targets_list]

print('|'.join(string_list))