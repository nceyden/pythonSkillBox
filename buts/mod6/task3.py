def is_armstrong_number(num):
    n = len(str(num))
    total = sum(int(digit) ** n for digit in str(num))
    return total == num

def get_armstrong_numbers():
    armstrong_numbers = []
    num = 10  # Начинаем с числа 10, так как числа 0-9 не учитываются
    while len(armstrong_numbers) < 8:
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
        num += 1
    return armstrong_numbers

result = get_armstrong_numbers()
print(' '.join(map(str, result)))
