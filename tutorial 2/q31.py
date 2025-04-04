from collections import Counter
n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
counts = Counter(numbers)
unique_numbers = []
for num in numbers:
    if counts[num] == 1:
        unique_numbers.append(num)
print("List after completely removing duplicates:", unique_numbers)
