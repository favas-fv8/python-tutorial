s = input("Enter a string: ")
mid = len(s) // 2
first_half = s[:mid][::-1]
second_half = s[mid:][::-1]
result = first_half + second_half
print("String after reversing first and second half separately:", result)
