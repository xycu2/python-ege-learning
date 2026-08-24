file = open('17.txt')
# -2
nums = []

for num in file:
    nums.append(int(num))

pairs = []

for i in range(len(nums) - 2):
    if (nums[i] + nums[i + 1] + nums[i + 2]) % 10 == 5 and (nums[i] * nums[i + 1] * nums[i + 2]) % 7 == 0:
        pairs.append(nums[i] + nums[i + 1] + nums[i + 2])

print(len(pairs), max(pairs))
