from collections import Counter
n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
counts = Counter(numbers)
max_count = max(counts.values())
mode = []
for num, count in counts.items():
    if count == max_count:
        mode.append(num)
print("Mode:", mode)
