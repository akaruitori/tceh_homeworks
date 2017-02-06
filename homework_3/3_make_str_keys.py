def make_str_keys(dictionary):
    """
    Задача 3. Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь.
    """
    return dict(zip([str(x) for x in dictionary.keys()], [dictionary[x] for x in dictionary]))

print(make_str_keys({1: 2, 3: 4, 5: 6}))
print(make_str_keys({(1,): 2, (3,): 4, (5,): 6}))
print(make_str_keys({None: 1}))
