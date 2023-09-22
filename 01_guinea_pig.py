quantity_food_in_kg = float(input())
quantity_hay_in_kg = float(input())
quantity_cover_in_kg = float(input())
guinea_weight_in_kg = float(input())

quantity_food_in_grams = quantity_food_in_kg * 1000
quantity_hay_in_grams = quantity_hay_in_kg * 1000
quantity_cover_in_grams = quantity_cover_in_kg * 1000
guinea_weight_in_grams = guinea_weight_in_kg * 1000
not_enough = False
days = 30

for day in range(1, days + 1):
    quantity_food_in_grams -= 300
    if day % 2 == 0:
        hay_needed = quantity_food_in_grams * 0.05
        quantity_hay_in_grams -= hay_needed
    if day % 3 == 0:
        cover_needed = guinea_weight_in_grams / 3
        quantity_cover_in_grams -= cover_needed

    if quantity_hay_in_grams <= 0 or\
            quantity_cover_in_grams <= 0 or\
            quantity_food_in_grams <= 0:
        not_enough = True
        break

if not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_grams / 1000:.2f},"
          f" Hay: {quantity_hay_in_grams / 1000:.2f}, Cover: {quantity_cover_in_grams / 1000:.2f}.")