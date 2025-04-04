for num in range(100, 1001):
    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    if sum_digits % 9 == 0:
        print(num)
