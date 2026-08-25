from fnmatch import fnmatch

for num in range(21025, 10**10 + 1, 21025):
    s = str(num)
    if fnmatch(s, '12*34?5'):
        evens = sum(1 for d in s if int(d) % 2 == 0)
        odds = len(s) - evens
        if evens == odds:
            print(num, num // 21025)


# 1214803475 57779
# 1233263425 58657
# 1240033475 58979
# 1241673425 59057
# 1258493425 59857
# 1265263475 60179
# 1283723425 61057