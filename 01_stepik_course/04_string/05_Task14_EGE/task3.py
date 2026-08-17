summ = 0

for x in '0123456789':
    for y in '0123456789':
        a1 = int('7' + y + x + '777', 13)
        a2 = int('6' + x + '66' + y + '6', 17)
        r = a1 + a2

        if r % 16 == 0:
            summ += r


print(summ)