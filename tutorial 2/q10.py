def is_valid_password(password):
    if len(password) < 6:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "$#@"
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True
    return has_lower and has_upper and has_digit and has_special
password = input("Enter password: ")
if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")
