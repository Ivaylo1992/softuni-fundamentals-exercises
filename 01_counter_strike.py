energy = int(input())
counter = 0
while True:
    
    command = input()

    if command == 'End of battle':
        print(f"Won battles: {counter}. Energy left: {energy}")
        break

    enemy_distance = int(command)

    if enemy_distance > energy:
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break

    energy -= enemy_distance
    counter += 1

    if counter % 3 == 0:
        energy += counter

