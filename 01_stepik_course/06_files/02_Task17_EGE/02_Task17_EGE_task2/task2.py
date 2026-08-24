file = open('17.txt')
nums = []

for num in file:
    nums.append(int(num))

pairs = []
minNum = min(nums)

for i in range(len(nums) - 1):
    if nums[i] % 117 == minNum or nums[i + 1] % 117 == minNum:
        pairs.append(nums[i] + nums[i + 1])

print(len(pairs), max(pairs))

