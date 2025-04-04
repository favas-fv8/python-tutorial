n = int(input("Enter number of elements: "))
s = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        s += num
print("Sum of even numbers:", s)
