def join_lists(*lists):
    """
    Задача 7. Написать функцию, которая принимает любое количество
    аргументов - списков, она должна возвращать список из всех объектов
    списков, но каждый объект должен быть уникальным.
    join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c']
    """
    result = []
    for lst in lists:
        for item in lst:
            if item not in result:
                result.append(item)
    return result

def join_lists2(*lists):
    """
    Другой вариант решения.
    """
    result = []
    for lst in lists:
        result.extend(lst)
    return list(set(result))

print(join_lists([], [''], [1], [12], [25, 43, 25], [1, 25, 34, 12, '']))
# 10000 loops, best of 3: 45.9 µs per loop

print(join_lists2([], [''], [1], [12], [25, 43, 25], [1, 25, 34, 12, '']))
# 10000 loops, best of 3: 37.8 µs per loop
