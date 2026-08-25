from fnmatch import  fnmatch

def evenNumbers(num):
    evenNum = 0

    for n in num:
        number = int(n)
        if number % 2 == 0:
            evenNum += 1

    return  evenNum


def oddNumbers(num):
    oddNum = 0

    for n in num:
        number = int(n)

        if number % 2 != 0:
            oddNum += 1

    return  oddNum

for num in range(21025, 10 ** 10 + 1, 21025):
    string = str(num)
    if fnmatch(string, '12*34?5') and (evenNumbers(string) == oddNumbers(string)):
        print(num, num // 21025)


# 1214803475 57779
# 1233263425 58657
# 1240033475 58979
# 1241673425 59057
# 1258493425 59857
# 1265263475 60179
# 1283723425 61057