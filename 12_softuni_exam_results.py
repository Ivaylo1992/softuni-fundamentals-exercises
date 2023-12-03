results_dict = {}
count_dict = {}
while True:
    command = input()

    if command == 'exam finished':
        break

    data = command.split('-')
    
    if len(data) == 2:
        username = data[0]
        if username in results_dict:
            del results_dict[username]
    elif len(data) == 3:
        username, language, points = data[0], data[1], int(data[2])

        if language not in count_dict:
            count_dict[language] = 0
        count_dict[language] += 1
        if username not in results_dict:
            results_dict[username] = {}
        if language not in results_dict[username]:
            results_dict[username][language] = points
        elif language in results_dict[username] and results_dict[username][language] < points:
            results_dict[username][language] = points

print('Results:')
for student, submissions in results_dict.items():
    print(f'{student} | {sum(submissions.values())}')

print('Submissions:')
for language in count_dict:
    print(f'{language} - {count_dict[language]}')
