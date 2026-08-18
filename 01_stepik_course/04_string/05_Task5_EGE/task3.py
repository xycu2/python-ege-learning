for n in range(11, 1000):
    b = bin(n)[2:]
    b = b[:-2] + '11'
    b = '11' + b
    b = b[0] + '00' + b[3:]

    r = int(b, 2)
    if r > 42:
        print(n)
        break