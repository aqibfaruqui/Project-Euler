def even(n):
    return n / 2

def odd(n):
    return 3*n + 1

max_count, max_i = 0, 0
curr = 0
for i in range(500000, 1000000):
    count = 0
    curr = i
    while i != 1:
        count += 1
        i = even(i) if i % 2 == 0 else odd(i)
    if count > max_count:
        max_count = count
        max_i = curr

print(max_i)
