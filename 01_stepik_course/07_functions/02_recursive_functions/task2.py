def odd_factorial(n):
    if n <= 1:
        return 1


    if n % 2 != 0:
        return n * odd_factorial(n - 1)
    else:
        return  odd_factorial(n - 1)
