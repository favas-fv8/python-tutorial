import math
x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))
sin_x = 0
for i in range(n):
    term = ((-1)**i * (x**(2*i+1))) / math.factorial(2*i+1)
    sin_x += term
print(sin_x)
