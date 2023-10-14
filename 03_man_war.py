pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))

max_health_capacity = int(input())
min_health_capacity = max_health_capacity * 0.2

while True:

    command = input().split()

    if command[0] == 'Retire':
        break
    elif command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship_status)):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(pirate_ship_status)) and end_index in range(len(pirate_ship_status)):
            for hit in range(start_index, end_index +1):
                pirate_ship_status[hit] -= damage
                if pirate_ship_status[hit] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship_status)):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity
    elif command[0] == 'Status':
        sections_to_repair = 0
        for section in pirate_ship_status:
            if section < min_health_capacity:
                sections_to_repair += 1
        print(f"{sections_to_repair} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
