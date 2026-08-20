n = int(input())
data = []
for i in range(n):
    new = int(input()) # считывание очередного значения
    data += [new] # добавление значения в список

mishaSumm = 0
zhannaSumm = 0
for elem in data:
    if elem % 2 == 0:
        mishaSumm += elem
    else:
        zhannaSumm += elem

print(mishaSumm)
print(zhannaSumm)