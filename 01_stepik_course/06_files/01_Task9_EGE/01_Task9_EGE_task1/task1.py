file = open('9.txt')
count = 0
for line in file:

    # создаем список на лету и сортируем его
    nums = sorted([int(x) for x in line.split()])

    # проверяем условие
    if nums[2] ** 2 > (nums[0] * nums[1]) * 2:
        count += 1

print(count)

