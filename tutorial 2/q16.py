def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_sign(num):
    if num > 0:
        print("Positive")
    if num < 0:
        print("Negative")
    if num == 0:
        print("Zero")
def factors(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")

choice = int(input("1. Even/Odd\n2. Positive/Negative/Zero\n3. Factors\nEnter choice: "))
num = int(input("Enter number: "))
if choice == 1:
    check_even_odd(num)
if choice == 2:
    check_sign(num)
if choice == 3:
    factors(num)
