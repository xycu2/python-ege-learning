file = open('17.txt')
nums = []

for num in file:
    nums.append(int(num))

pairs = []

for i in range(len(nums) - 1):
    if (nums[i] * nums[i + 1] > 0) and ((nums[i] + nums[i + 1]) % 7 == 0):
        pairs.append(nums[i] * nums[i + 1])

print(len(pairs), min(pairs))