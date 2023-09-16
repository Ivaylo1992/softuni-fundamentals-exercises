input_line = input()

#empty list to store the indexes in it
my_list = []

#loop over the string and find the capital letters
for i in range(len(input_line)):
    if input_line[i].isupper():
        my_list.append(i)

#result
print(my_list)

