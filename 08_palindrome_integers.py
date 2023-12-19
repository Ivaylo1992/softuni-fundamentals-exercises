num_list = list(map(int, input().split(', ')))


def palindrome_integer(num):
    num_to_str = str(num)
    if num == int(num_to_str[::-1]):
        return True
    else:
        return False


for num in num_list:
    print(palindrome_integer(num))