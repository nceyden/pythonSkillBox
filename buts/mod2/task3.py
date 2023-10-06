numbers_str = input()
a_endPos = numbers_str.find(' ') # ищем подстроку до первого пробела
a = int(numbers_str[:a_endPos]) # подстрока до первого пробела - число а
b_startPos = a_endPos + 1 # находим начало подстроки числа b
b_endPos = numbers_str.find(' ', b_startPos) # находим конец подстроки числа b
b = int(numbers_str[b_startPos:b_endPos]) # вычлиняем его
c = int(numbers_str[b_endPos + 1:]) # конец подстроки b + 1 = начало подстроки c

if not((a < -1000) or (a > 1000) or (b < -1000) or (b > 1000) or (c < -1000) or (c >1000)):

    if a <= b <= c or c <= b <= a:
        print(b)
    elif b <= a <= c or c <= a <= b:
        print(a)
    else:
        print(c)
else: exit