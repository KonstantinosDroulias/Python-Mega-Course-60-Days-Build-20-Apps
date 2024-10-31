from unicodedata import digit

password = input("Enter password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
uppercase = False
for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        uppercase = True

result["digits"] = digit
result["upper-case"] = uppercase


print(result)
print(result.values())

if all(result.values()):
    print("Strong Password")
elif sum(result.values()) == 2:
    print("Medium Password")
else:
    print("Week Password")
