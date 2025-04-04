s = input("Enter a string: ")
even_index_chars = ""
odd_index_chars = ""
for i in range(len(s)):
    if i % 2 == 0:
        even_index_chars += s[i]
    if i % 2 != 0:
        odd_index_chars += string[i]
print("Characters at even indices:", even_index_chars)
print("Characters at odd indices:", odd_index_chars)
