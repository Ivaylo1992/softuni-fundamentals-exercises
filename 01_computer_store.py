#challenge Computer Store from SoftUni fundamentals
total_price = 0

while True:
    input_line = input()

    if input_line.isalpha():
        taxes = total_price * 0.2
        total_price_with_taxes = taxes + total_price

        if total_price == 0:
            print('Invalid order!')
            break

        if input_line == 'special':
            discount_price = total_price_with_taxes * 0.9
        break

    price = float(input_line)
    if price < 0:
        print("Invalid price!")
        continue

    total_price += price

if total_price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    
    if input_line == 'special':
        print(f'Total price: {discount_price:.2f}$')
    else:
        print(f'Total price: {total_price_with_taxes:.2f}$')
