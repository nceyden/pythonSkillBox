def func(a, b):
    if b == 0:
        return a
    else:
        return func(b, a % b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"Наибольший общий делитель: {func(a, b)}")
