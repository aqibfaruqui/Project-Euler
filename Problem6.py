sumOfSquares = 0
squareOfSums = 0
square = 0
sum = 0

for i in range(1, 101):
    square = i * i
    sumOfSquares += square

for i in range(1, 101):
    sum += i

squareOfSums = sum * sum

print(squareOfSums - sumOfSquares)