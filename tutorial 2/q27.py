def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter number of elements: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
primes = []
composites = []
for num in numbers:
    if num > 1 and is_prime(num):
        primes.append(num)
    if num > 1 and not is_prime(num):
        composites.append(num)
print("Prime numbers:", primes)
print("Composite numbers:", composites)
