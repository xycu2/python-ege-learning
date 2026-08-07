n = int(input())
summ = 0

for i in range(n):
    stock = int(input())

    if stock % 13 != 0:
        summ += stock


print(summ)