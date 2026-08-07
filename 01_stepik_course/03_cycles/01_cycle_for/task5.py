num = int(input())
watermelon = 0
melon = 0


for i in range(num):
    name = input()

    if name == 'дыня':
        melon += 1
    elif name == 'арбуз':
        watermelon += 1

if melon > watermelon:
    print('Дыни популярнее')
elif watermelon > melon:
    print('Арбузы популярнее')
else:
    print('Арбузы и дыни одинаково популярны')