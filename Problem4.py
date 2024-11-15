def palindrome(x, y):
    a = str(x * y)
    length = len(a)
    if length == 5:
        if a[0] == a[4] and a[1] == a[3]:
            return True
    if length == 6:
        if a[0] == a[5] and a[1] == a[4] and a[2] == a[3]:
            return True
    return False

largestPalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome(i, j):
            if i * j > largestPalindrome:
                largestPalindrome = i * j

print(largestPalindrome)


        

