registrations_count = int(input())
registrations = {}

for user in range(registrations_count):
    line = input().split()
    command = line[0]
    if command == 'register':
        name, plate = line[1], line[2]
        if name in registrations:
            print(f"ERROR: already registered with plate number {registrations[name]}")
        else:
            registrations[name] = plate
            print(f"{name} registered {plate} successfully")
    elif command == 'unregister':
        name = line[1]
        if name not in registrations:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del registrations[name]

for k, v in registrations.items():
    print(f"{k} => {v}")