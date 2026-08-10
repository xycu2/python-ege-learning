n = int(input())

# отвечает за вертикаль
for x in range(1, n + 1):
    # отвечает за горизонталь
    for y in range(1, n + 1):
        print(f'{x} * {y} = {x * y}', end='    ')
    print()