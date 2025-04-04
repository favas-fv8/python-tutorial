s = input("Enter a string: ")
is_palindrome = True
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
