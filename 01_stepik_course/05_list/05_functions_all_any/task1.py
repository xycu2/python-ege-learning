text = input().split()

bool_status = [s == 'True' for s in text]

print(all(bool_status))