num = input()
summ = 0


while num != 'СТОП':
    val = int(num)
    if (val < 0) and (val % 2 != 0):
       summ += 1

    num = input()

print(summ)