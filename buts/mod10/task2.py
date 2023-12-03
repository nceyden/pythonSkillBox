import requests
import re
from bs4 import BeautifulSoup

def extract_text(url, tag, attribute=None, attribute_value=None):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    if attribute and attribute_value:
        result = soup.find_all(tag, {attribute: re.compile(attribute_value)})
    else:
        result = soup.find_all(tag)

    return [element.get_text() for element in result]

# ввод данных из консоли (адрес сайта, тег, атрибут и его значение)
url = input("Введите URL сайта: ")
tag_to_search = input("Введите тег для поиска (н-р, h3): ")
attribute_to_search = input("Введите атрибут для поиска (или нажмите Enter, если нет): ")
attribute_value_to_search = input("Введите значение атрибута (или нажмите Enter, если нет): ")

# извлечение текста
result = extract_text(url, tag_to_search, attribute_to_search, attribute_value_to_search)
print(result)
