def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
sort_list(numbers)
print("Sorted list:", numbers)
