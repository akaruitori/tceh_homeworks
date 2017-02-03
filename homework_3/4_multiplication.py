from functools import reduce


def multiplication2(num_list):
    """
    Задача 4. Написать функцию, которая принимает список чисел и возвращает их произведение.
    """
    return reduce(lambda x, y: x * y, num_list)