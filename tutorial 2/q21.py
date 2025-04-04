n = int(input("Enter number of elements: "))
total = 0
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        total += num
print(total)
