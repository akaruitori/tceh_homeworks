import re
import requests


"""
1. Прочитать теорию (ссылки в материалах) о работе с файлами в python.
И реализовать две функции: write_to_file(data) и read_file_data().
Которые соотвественно: пишут данные в файл и читают данные из файла.
"""


def write_to_file(data):
    """
    Добавляет в конец файла test.txt текст data.
    data: строка
    """
    with open('test.txt', 'w') as test_file:
        test_file.write(data)
    test_file.close()


def read_file_data():
    """
    Возвращает строковое содержимое файла test.txt
    """
    with open('test.txt', 'r') as test_file:
        data = test_file.read()
    test_file.close()
    return data


"""
2. Прочитать теорию о работе с json. Реализовать следующую логику:
получать при помощи requests данные сайта
https://jsonplaceholder.typicode.com/, выводить в консоль все пары
"ключ-значение", сохранять полученный json в файл.
"""


def save_json_data():
    """
    Забирает JSON-контент со страницы
    'https://jsonplaceholder.typicode.com/posts/'
    Выводит ключи и значения в консоль, записывает данные в файл с помощью
    функции из 1 задачи.
    """
    data = requests.get('https://jsonplaceholder.typicode.com/posts/').json()
    for line in data:
        for k, v in line.items():
            print(k, ':', v)
    write_to_file(str(data))


"""
3. Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы
на другие.
"""


def parse_links_from(url):
    """
    Собирает все ссылки со страницы c заданным url, кроме ведущих на
    страницы на https://habrahabr.ru
    :return: список строк с url
    """
    data = requests.get(url)
    pattern = r'<a href="(http\S*)[^(https://habrahabr.ru\)]"'
    links = re.findall(pattern, str(data.content))
    return links


if __name__ == '__main__':

    print('Задача 1:')
    write_to_file('Hello world!')
    print(read_file_data())

    print('\nЗадача 2:')
    save_json_data()

    print('\nЗадача 3:')
    links = parse_links_from('https://habrahabr.ru/')
    print(links)
