CAPACITY = 255
liters_poured = 0
n = int(input())

for _ in range(n):
    liters = int(input())
    if CAPACITY < liters:
        print('Insufficient capacity!')
        continue

    CAPACITY -= liters
    liters_poured += liters

print(liters_poured)
