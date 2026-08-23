n = int(input())
result = [input() for _ in range(n)]
result = [word for word in result if len(word) > 6]
print(*result)
