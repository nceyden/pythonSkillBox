telephone_number = input()
new_phone_number = ""

for char in telephone_number:
    if char.isnumeric() or char == '+':
        new_phone_number += char

print(new_phone_number)
