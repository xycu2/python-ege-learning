h = int(input())

count = 0
cube = 1
total_height = 0

while total_height <= h:
    total_height += cube
    count += 1
    cube += 1

print(count)