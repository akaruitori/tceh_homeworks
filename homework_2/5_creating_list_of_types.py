def find_types(*args):
    """
    Задача 5. Написать функцию, которая принимает любое количество аргументов, возвращает список типов
    принятых аргументов find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]
    """
    result = []
    for item in args:
        result.append(type(item))
    return result