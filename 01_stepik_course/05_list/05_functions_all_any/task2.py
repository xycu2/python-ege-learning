points = [int(input()) for _ in range(int(input()))]
result = [point == 100 for point in points]

print(any(result))