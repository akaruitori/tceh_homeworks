def sort_list(int_list):
    """
    Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его.
    Иначе выбрасывает ValueError.
    """
    for item in int_list:
        if type(item) != int:
            raise ValueError
    return sorted(int_list)
