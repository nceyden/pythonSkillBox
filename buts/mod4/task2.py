def func(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = func(a, n // 2) #чет
        return half_power * half_power
    else:
        return a * func(a, n - 1) #нечет

#пример
a = 2 #основание
n = 10 
result = func(a, n)

print(f"{a}^{n} = {result}")
