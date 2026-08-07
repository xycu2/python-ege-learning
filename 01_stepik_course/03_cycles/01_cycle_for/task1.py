num = int(input())
countRedCars = 0

for i in range(num):
    carsColor = input()
    if carsColor == 'красный':
        countRedCars += 1

print(countRedCars)