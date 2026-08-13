# 1
string = input()
finalString = ''

for i in range(len(string)):
    if i % 2 != 0:
        finalString += string[i]

print(finalString)


# 2
print(string[1::2])