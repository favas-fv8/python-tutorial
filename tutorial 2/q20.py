n = int(input("Enter number of names: "))
names = []
for _ in range(n):
    name = input()
    names.append(name)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]
print("Sorted names:", names)
