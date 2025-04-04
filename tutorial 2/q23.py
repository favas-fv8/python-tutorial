def find_median(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]
n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
median = find_median(numbers)
print("Median:", median)
