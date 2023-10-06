string = input()

count_zero = 0
count_one = 0

for char in string:
    if char == '0':
        count_zero += 1
    elif char == '1':
        count_one += 1

if count_zero == count_one:
    print('yes')
else:
    print('no')
