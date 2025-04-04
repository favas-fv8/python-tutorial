a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
sides = sorted([a, b, c])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")
