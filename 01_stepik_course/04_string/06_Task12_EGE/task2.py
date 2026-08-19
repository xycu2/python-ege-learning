max_mult_digit = -1
for n in range(4, 1000):
    s = '9' + '3' * n

    while '22' in s or '333' in s or '9999' in s:

        if '22' in s:
            s = s.replace('22', '3', 1)

        if '333' in s:
            s = s.replace('333', '99', 1)

        if '9999' in s:
            s = s.replace('9999', '22', 1)

    mult_digit = 1

    for digit in s:
        mult_digit *= int(digit)

    if mult_digit > max_mult_digit:
        max_mult_digit = mult_digit

print(max_mult_digit)
