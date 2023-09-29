moves = 1

data = list(input().split())

while True:
    input_line = input()

    if input_line == 'end':
        break

    guesses = input_line.split()

    first_index = int(guesses[0])
    second_index = int(guesses[1])

    if first_index == second_index or first_index not in range(len(data)) \
            or second_index not in range(len(data)):
        insert_index = len(data) // 2
        data.insert(insert_index, f'-{moves}a')
        data.insert(insert_index, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")
        moves += 1
    elif data[first_index] == data[second_index]:
        print(f"Congrats! You have found matching elements - {data[first_index]}!")
        first_element = data[first_index]
        second_element = data[second_index]
        data.remove(first_element)
        data.remove(second_element)
        moves += 1
    else:
        print("Try again!")

    if not data:
        print(f"You have won in {moves-1} turns!")
        break


if len(data) > 0:
    print("Sorry you lose :(")
    print(' '.join(data))