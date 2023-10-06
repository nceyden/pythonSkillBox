domain = input()
temp = ''
while True:
    if len(domain) > 0:
        current_str = domain[0]
        if current_str!= '.':
            temp += current_str
            domain = domain[1::]
        else:
            print(temp)
            domain = domain[1::]
            temp = ''
    else:
        print(temp)
        break
        