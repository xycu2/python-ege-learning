n = int(input())

plusList = []
minusList = []

for i in range(n):
    num = int(input())

    if num > 0:
        plusList += [num]
    elif num < 0:
        minusList += [num]

# 1
print(*plusList)
print(*minusList)

# 2
for num in plusList:
    print(num, end=' ')

print()

for num in minusList:
    print(num, end=' ')
