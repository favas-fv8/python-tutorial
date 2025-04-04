l, u = map(int, input("Enter lower and upper limit: ").split())
s = 0
for i in range(l, u+1):
    if i % 2 != 0:
        s += i
print("Sum of odd numbers:", s)
