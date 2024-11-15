def isPrime(x):
    for i in range(2, int((x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

sum = 0 

for i in range(3, 2000001, 2):
    if isPrime(i):
        print(i)
        sum = sum + i

sum += 2
print(sum)
