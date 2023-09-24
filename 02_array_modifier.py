input_line = list(map(int, input().split()))

while True:
    operations_input = input()
    if operations_input == 'end':
        break

    operations = operations_input.split()

    if operations[0] == 'swap':
        first_idx = int(operations[1])
        second_idx = int(operations[2])
        input_line[first_idx], input_line[second_idx] \
            = input_line[second_idx], input_line[first_idx]
    elif operations[0] == 'multiply':
        first_idx = int(operations[1])
        second_idx = int(operations[2])
        input_line[first_idx] *= input_line[second_idx]
    elif operations[0] == "decrease":
        for i in range(len(input_line)):
            input_line[i] -= 1


new_list = list(map(lambda num: str(num), input_line))

print(', '.join(new_list))