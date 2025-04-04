s = input("Enter a string: ")
if " " in s:
    print(s.replace(" ", "*"))
else:
    print("$" + s + "$")
