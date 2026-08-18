for n in range(1, 1000):
    b = bin(n)[2:]
    b += '00'
    b = '1' + b

    r = int(b, 2)

    if r > 400:
        print(n)
        break