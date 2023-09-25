nums = list(map(int, input().split()))
sorted_list = sorted(nums, reverse=True)
average_num = sum(nums) / len(nums)
top_five_list = []

for num in sorted_list:
    if num > average_num:
        top_five_list.append(num)

    if len(top_five_list) == 5:
        break

if not top_five_list:
    print('No')
else:
    for num in top_five_list:
        print(num, end=' ')
