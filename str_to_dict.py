#https://edabit.com/challenge/iG5vcwd282T4t7h6r
def str_to_dict(lst):
    new_dict = {}
    for item in lst:
        items = item.split('=')
        new_dict[items[0]] = items[1]

    return new_dict


print(str_to_dict(["1=one", "2=two", "3=three", "4=four"]))
print(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]))
print(str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]))
