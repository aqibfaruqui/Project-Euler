a = 600851475143
largestPrimeFactor = 0
subjectPrime = 0

def isPrime(x):
    for i in range(2, int((x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

def prime():
    global subjectPrime, largestPrimeFactor
    for i in range(2, int((a ** 0.5) + 1)):
        if isPrime(i):
            if a % i == 0:
                pair = a // i
                if isPrime(pair) and pair > i:          # Checks if pair of prime factor is also prime and larger
                    largestPrimeFactor = pair
                else:
                    largestPrimeFactor = i

prime()
print(largestPrimeFactor)