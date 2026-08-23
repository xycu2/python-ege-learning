numbers = [int(input()) for _ in range(int(input()))]
resultNum = [number % 10 == 7 for number in numbers]

print(all(resultNum))