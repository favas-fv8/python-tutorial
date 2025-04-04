n = int(input("Enter a number: "))
s = 0
for i in range(2, n+1, 2):
    s += i**3
print("Sum of cubes:", s)
