'''Counting Collatz conjecture'''

def even(n):
    n = n / 2
    return n

def odd(n):
    n = 3*n + 1
    return n

def counting(n):
    counter = 0
    while True:
        counter += 1
        if n == 1:
            print(counter)
            return
        elif n % 2 == 0:
            even(n)
        elif n % 2 == 1:
            odd(n)

counting(5)

