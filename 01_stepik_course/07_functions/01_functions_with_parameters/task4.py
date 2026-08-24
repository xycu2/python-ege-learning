def sum_even_dig(number):
    numStr = str(number)
    count = 0
    for num in numStr:
        b = int(num)
        if b % 2 == 0:
            count += b

    if count > 0:
        return count
    else:
        return 0
