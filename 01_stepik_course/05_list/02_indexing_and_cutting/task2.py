list = []
list_square = []
list_cube = []

for i in range(1, 11):
    list += [i]

for list2 in list:
    list_square += [list2 ** 2]


for list3 in list:
    list_cube += [list3 ** 3]

print(*list)
print(*list_square)
print(*list_cube)