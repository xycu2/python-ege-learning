maxSum = int(input())
pricesProduct = input().split()

bool_status = [int(prod) <= maxSum for prod in pricesProduct]

print(any(bool_status))