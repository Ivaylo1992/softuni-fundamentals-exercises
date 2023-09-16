number = int(input())

#creating a list from the charecters of the string of our integer input
lst_num = [int(char) for char in str(number)]

#sorting the numbers from the largest to the smallest one
max_num_lst = sorted(lst_num, reverse=True)

#making a list of strings from the numbers in order to join them after in a single string
max_num_str = [str(num) for num in max_num_lst]

# print the result
print((int(''.join(max_num_str))))
