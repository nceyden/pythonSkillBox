input_string = input()

comma_index = input_string.index(',') # Разделим входную строку на символ и смещение
letter = input_string[0]
n = int(input_string[comma_index + 1:])

if 'a' <= letter <= 'z':
    unicode_value = ord(letter) - ord('a')
    shifted_unicode = (unicode_value + n) % 26
    result_letter = chr(shifted_unicode + ord('a'))
    print(result_letter)
else:
    print("Неверный ввод")
