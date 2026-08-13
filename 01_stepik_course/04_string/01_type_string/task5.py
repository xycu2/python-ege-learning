n = int(input())
maxString = ''

for i in range(n) :
    string = input()

    if len(string) > len(maxString):
        maxString = string

print(maxString * 3)