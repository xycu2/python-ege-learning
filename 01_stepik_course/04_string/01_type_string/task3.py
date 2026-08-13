n = int(input())
summString = 0

for i in range(n):
    sting = input()

    if ('d' in sting) and ('w' in sting):
        summString += 1

print(summString)