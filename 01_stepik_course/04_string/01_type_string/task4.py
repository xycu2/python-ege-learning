str1 = input()
str2 = input()
str3 = input()


if str1 == str2 == str3:
    print('EQUAL')
elif str1 != str2 and str2 != str3 and str1 != str3:
    print('DIFFERENT')
else:
    print('BINGO!')