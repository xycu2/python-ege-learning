n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

d = nums[1] - nums[0]

flag = True

for i in range(2, n):
    if nums[i] - nums[i - 1] != d:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')

