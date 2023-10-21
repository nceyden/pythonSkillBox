def func(numbers):
    if all(x == numbers[0] for x in numbers):
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

numbers_string = input("")
numbers = [int(x) for x in numbers_string.split()]

print(func(numbers))
