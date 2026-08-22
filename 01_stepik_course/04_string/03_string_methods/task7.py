price = input().split()

for i in range(len(price)):
    price[i] = int(price[i])

even = 0
notEven = 0

for num in price:
    if num % 2 == 0:
        even += 1
    else:
        notEven += 1

if even == notEven:
    print(f'Поровну {sum(price)}')
elif even > notEven:
    print(f'Михаил {sum(price)}')
else:
    print(f'Жанна {sum(price)}')

