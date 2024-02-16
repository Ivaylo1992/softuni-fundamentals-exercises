#https://edabit.com/challenge/KEz3TAQfh9WxSZMLH

def count_all(input_string):
    letters_count = 0
    digits_count = 0
    count_dict = {}
    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1

    count_dict['LETTERS'] = letters_count
    count_dict['DIGITS'] = digits_count

    return count_dict


print(count_all("Hello World"))
print(count_all("149990"))

