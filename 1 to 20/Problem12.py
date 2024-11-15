def checkDivisors(x):
    divisors = []
    i = 1
    while i < x**0.5:
        if x % i == 0:
            divisors.append(i)
            divisors.append(x/i)
        i += 1
    return len(divisors)

def triangleNumber():
    x = 0
    i = 0
    while True:
        i += 1
        x = x + i
        if checkDivisors(x) > 500:
            print(x)
            break

triangleNumber()