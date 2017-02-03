"""
Задача 5. Написать три функции: do_work, handle_success, handle_error. do_word(my_list, success_callback,
error_callback) принимает на вход три аргумента: список, функцию для обработки успеха и функцию для обработки ошибки.
Ее задача проверить, что все значения в списке идут по-возрастанию. Если все верно: вызываем success_callback, иначе:
error_callback. Функция handle_success пишет в консоль информацию об успешном выполнении. Функция handle_error
выбрасывает ValueError
"""

def do_work(my_list, success_callback, error_callback):
    if my_list == sorted(my_list):
        success_callback()
    else:
        error_callback()

def handle_succes():
    print('Успех!')

def handle_error():
    raise ValueError