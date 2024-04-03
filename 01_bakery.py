input_line = input().split(' ')


def bakery_prices(lst):
    price_dict = {}
    for i in range(0, len(lst)-1, 2):
        price_dict[lst[i]] = int(lst[i+1])

    return price_dict


print(bakery_prices(input_line))
