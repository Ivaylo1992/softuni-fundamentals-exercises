#https://edabit.com/challenge/kSmkcYLcWRnEEwXwX
def calculate_losses(loses_dict):
    if not loses_dict:
        return 'Lucky you!'
    else:
        return sum(loses_dict.values())


print(calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}))

print(
calculate_losses({
  "painting" : 20000,
}))