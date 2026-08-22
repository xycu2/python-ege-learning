res = [int(input()) for _ in range(int(input()))]
x = int(input())
finalRes = [n for n in res if n > x]
print(*finalRes)