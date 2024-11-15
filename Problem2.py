current = 0
sum = 0

a = 1
b = 2
tmp1 = 0

while current < 4000000:
    current = b
    if current % 2 == 0:
        sum += current
    prevA = a
    a = b
    b = prevA + b

print(sum)

    




