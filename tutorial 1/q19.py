n = int(input("Enter count: "))
even, odd = 0, 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count:", even)
print("Odd count:", odd)
