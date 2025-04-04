n = int(input("Enter number of elements: "))
lst = []
for _ in range(n):
    element = input()
    try:
        if '.' in element:
            lst.append(float(element))
        else:
            lst.append(int(element))
    except ValueError:
        lst.append(element)
integers = []
floats = []
strings = []
for item in lst:
    if isinstance(item, int):
        integers.append(item)
    if isinstance(item, float):
        floats.append(item)
    if isinstance(item, str):
        strings.append(item)
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
