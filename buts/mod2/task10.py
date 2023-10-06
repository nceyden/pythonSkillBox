string = input()

new_word = "" # строка для новых последних букв

current_word = "" # для отслеживания текущего слова

for char in string:
    if char != ' ':
        current_word += char
    else:
        if current_word:
            new_word += current_word[-1] # Если текущий символ - пробел, то текущее слово завершено.
            current_word = "" # Добавим последний символ этого слова к новому слову и сбросим текущее слово.
if current_word:
    new_word += current_word[-1] # если текущее слово осталось и добавим его последнюю букву к новому слову

# Выведем результат
print(new_word)
