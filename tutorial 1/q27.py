import math
a, b, c = map(float, input("Enter a, b, c: ").split())
d = b**2 - 4*a*c
if d > 0:
    print((-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))
elif d == 0:
    print(-b / (2*a))
else:
    print("No real roots")
