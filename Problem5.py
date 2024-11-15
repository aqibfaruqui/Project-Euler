def check(x):   
    for i in range(11, 21):     # Div by 11 to 20 also maintaind div by 1 to 10
        if x % i != 0:
            return False
    return True

num = 2520                      # num < 2520 does not divide by 1 to 10
while num:
    if check(num):
        break
    num += 10               # Must be divisible by 10

print(num)

# 20 divides 2, 4, 5, 10 
# 19
# 18 divides 3, 6, 9
# 17
# 16 divides 8
# 15
# 14 divides 7
# 13
# 12
# 11