number = int(input())
maxNum = -1

for i in range(number):
    countNum = int(input())

    if countNum > maxNum:
        maxNum = countNum

print(maxNum)
