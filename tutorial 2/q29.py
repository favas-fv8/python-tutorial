n1 = int(input("Enter number of elements in set A: "))
A = set()
for _ in range(n1):
    A.add(int(input()))
n2 = int(input("Enter number of elements in set B: "))
B = set()
for _ in range(n2):
    B.add(int(input()))
union_set = A | B
intersection_set = A & B
difference_A_B = A - B
difference_B_A = B - A
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference A - B:", difference_A_B)
print("Difference B - A:", difference_B_A)
