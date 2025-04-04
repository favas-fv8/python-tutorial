numbers = []
for _ in range(4):
    num = int(input())
    numbers.append(num)
sum_positive = 0
count_positive = 0
sum_negative = 0
count_negative = 0
for num in numbers:
    if num > 0:
        sum_positive += num
        count_positive += 1
    if num < 0:
        sum_negative += num
        count_negative += 1
if count_positive > 0:
    avg_positive = sum_positive / count_positive
else:
    avg_positive = 0
if count_negative > 0:
    avg_negative = sum_negative / count_negative
else:
    avg_negative = 0
print("Sum of positive numbers:", sum_positive)
print("Average of positive numbers:", avg_positive)
print("Sum of negative numbers:", sum_negative)
print("Average of negative numbers:", avg_negative)
