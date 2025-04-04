x = int(input("Enter X: "))
y = int(input("Enter Y: "))
result = 1
for i in range(abs(y)):
    result *= x
if y < 0:
    result = 1 / result
print(result)
