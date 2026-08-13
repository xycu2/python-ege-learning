n = int(input())
count = 0

for i in range(n):
    string = input()

    if string[0] == string[-1]:
        count += 1

print(count)