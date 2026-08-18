for n in range(10000, 1, -1):
    b = bin(n)[2:]

    if b.count('1') > b.count('0'):
        b += '00'
    elif b.count('0') > b.count('1'):
        b += '11'
    else:
        b += '10'

    r = int(b, 2)

    if r <= 1000:
        print(n)
        break
