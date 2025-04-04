n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)
