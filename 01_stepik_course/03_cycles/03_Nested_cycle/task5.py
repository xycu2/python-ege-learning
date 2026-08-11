quantity = int(input())

for i in range(quantity):
    name = input()
    total_sum = 0
    count = 0
    for y in range(4):
        grade = int(input())
        total_sum += grade
        count += 1

    avg = total_sum / count
    final_grade = int(avg + 0.5)

    print(f'{name} - {final_grade}')