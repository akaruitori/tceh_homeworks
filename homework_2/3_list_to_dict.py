def count_types(lst):
    """
    Задача 3. Написать функцию, которая принимает список, и возвращает словарь в формате:
    "тип данных: количество объектов" count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}
    """
    dct = {}
    for item in lst:
        if type(item) not in dct:
            dct[type(item)] = 1
        else:
            dct[type(item)] += 1
    return dct