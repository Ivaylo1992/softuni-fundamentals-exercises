houses = list(map(int, input().split('@')))
index = 0
while True:
    command = input()

    if command == "Love!":
        break

    jump_command = command.split()
    jump_length = int(jump_command[1])

    current_house = index + jump_length

    if current_house > len(houses) - 1:
        current_house = 0

    houses[current_house] -= 2

    if houses[current_house] < 0:
        print(f"Place {current_house} already had Valentine's day.")

    elif houses[current_house] == 0:
        print(f"Place {current_house} has Valentine's day.")

    index = current_house


houses = [1 for num in houses if num > 0]

if sum(houses) == 0:
    print(f"Cupid's last position was {index}.")
    print("Mission was successful.")
else:
    print(f"Cupid's last position was {index}.")
    print(f"Cupid has failed {sum(houses)} places.")