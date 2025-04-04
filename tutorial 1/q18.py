n = int(input("Enter a number: "))
num_digits = len(str(n))
sum_of_powers = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
if sum_of_powers == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
