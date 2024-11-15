triplet = []
abc = 0

def checkSum1000(x):
    if x[0] + x[1] + x[2] == 1000:
        return True
    return False

for i in range(1, 400):
    for j in range(1, 400):
        triplet.clear()
        sum = i ** 2 + j ** 2
        c = sum ** 0.5
        if round(c) == c:
            c = int(c)
            triplet.extend([i, j, c])
            if checkSum1000(triplet):
                print(triplet)
                abc = i * j * c

print(abc)


