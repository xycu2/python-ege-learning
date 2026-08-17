summ = 0

for x in '0123456789':
    a1 = int('84' + x + '9999', 14)
    a2 = int('1' + x + '765', 16)
    r = a1 + a2

    if r % 6 == 0:
        summ += r

mult = 1
for digit in str(summ):
    if digit != '0':
        mult *= int(digit)

print(mult)
