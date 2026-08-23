file = open('9.txt')
count = 0

for line in file:
    nums = sorted([int(x) for x in line.split()])
    summ1 = nums[0] + nums[-1]
    summ2 = nums[1] + nums[2]

    if summ1 <= summ2:
        count += 1

print(count)
