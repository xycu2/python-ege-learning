for x in '0123456789':
    a1 = '98' + x + '123'
    a2 = '111' + x + '222'
    r = int(a1, 19) + int(a2, 19)

    if r % 14 == 0:
        print(r // 14)
        break