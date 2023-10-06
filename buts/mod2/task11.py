def has_duplicate_digits(numbers):

    for i in range(len(numbers)):
        if numbers[i].isdigit():

            digit_i = int(numbers[i])
            for j in range(i + 1, len(numbers)):
                if numbers[j].isdigit():
                    digit_j = int(numbers[j])
                    if digit_i == digit_j:
                        return True
    return False

numbers = input("Введите последовательность целых чисел: ")

result = has_duplicate_digits(numbers)
print(result)
