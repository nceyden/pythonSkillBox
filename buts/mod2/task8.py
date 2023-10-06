string = input()


s_endPos = string.find(',')
s = string[:s_endPos]
i = string[s_endPos + 2:]
print(s, i)
count = 0

for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)
