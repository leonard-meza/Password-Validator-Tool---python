# minimum length 8 characters
# must contain one or more alphabetical [a-z]
# must contain one or more Uppercase characters [A-Z]
# must contain one or more numeric characters [0-9]
# must contain one or more special characters [_$!]

import re

with open(r'C:\Users\Lsmfa\Desktop\fakepasswords.txt') as file:
    for i in file:
        for password in i.split():
            if len(password) < 8:
                print("Attention '{password}' is a not a strong enough password. Password length must be at least 8 upper and lower case characters, at least one number, with one of these special characters _@$")
            elif not re.search("[a-z]", password):
                print(f"Attention '{password}' is a not a strong enough password. Password length must be at least 8 upper and lower case characters, at least one number, with one of these special characters _@$")
            elif not re.search("[A-Z]", password):
                print(f"Attention '{password}' is a not a strong enough password. Password length must be at least 8 upper and lower case characters, at least one number, with one of these special characters _@$")
            elif not re.search("[0-9]", password):
                print(f"Attention '{password}' is a not a strong enough password. Password length must be at least 8 upper and lower case characters, at least one number, with one of these special characters _@$")
            elif not re.search("[_@$]" , password):
                print(f"Attention '{password}' is a not a strong enough password. Password length must be at least 8 upper and lower case characters, at least one number, with one of these special characters _@$")
            else:
                print(f"Congratulations '{password}' is a strong password.")

