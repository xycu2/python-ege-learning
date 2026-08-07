num = int(input())
maxSumm = 0
minSumm = 0

for i in range(num):
    price = int(input())

    if i == 0:
        maxSumm = price
        minSumm = price
    else:
        if price > maxSumm:
            maxSumm = price

        if price < minSumm:
            minSumm = price

print(maxSumm + minSumm)
