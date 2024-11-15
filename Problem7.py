def isPrime(x):
    for i in range(2, int((x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

num = 0
i = 2

while True:
    if isPrime(i):
        num += 1
        if num == 10001:
            print(i)
            break
    i += 1