# 1
string = input()[1::2]
summ = 0

for num in string:
    digit = int(num)
    if digit % 2 == 0:
        summ += digit

print(summ)

# 2
string1 = input()[1::2]
summ1 = 0


for i in range(len(string1)):
    if int(string1[i]) % 2 == 0:
        summ1 += int(string1[i])

print(summ1)