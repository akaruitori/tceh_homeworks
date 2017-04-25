def compare_dicts(dict_a, dict_b):
    """
    Задача 4. Написать функцию, которая принимает два словаря, сравнивает их ключи,
    выдает в консоль сколько у них общих ключей.
    """
    common_keys = 0
    for key_a in dict_a:
        for key_b in dict_b:
            if key_a == key_b:
                common_keys += 1
    print('Общих ключей: ', common_keys)

# Альтернативный короткий вариант решения 4 задачи:
def compare_dicts2(dict_a, dict_b):
    print('Общих ключей: ', len(dict_a.keys() & dict_b.keys()))


