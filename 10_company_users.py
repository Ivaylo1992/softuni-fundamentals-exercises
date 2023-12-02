companies_users = {}

while True:

    command = input()

    if command == 'End':
        break

    company, ID = command.split(' -> ')

    if company not in companies_users:
        companies_users[company] = []

    if ID not in companies_users[company]:
        companies_users[company].append(ID)


for company in companies_users:
    print(company)
    for id in companies_users[company]:
        print(f'-- {id}')
