'''
Задача 2. Написать функцию для определения НОК для двух чисел.

Я выбрала способ расчета через наибольший общий делитель: НОК(х, у) = |х * у| / НОД(х, у)

'''


def gcd(a, b):
        """
        Поиск НОД по методу Евклида:
        НОД (x, y) = НОД (у, x % y), учитывая, что НОД (a, 0) = а. Напрашивается рекурсивное решение.
        """
        if b == 0:
            return abs(a)
        else:
            return gcd(b, a % b)


def lcm(a, b):
    if a == b and b == 0:  # Защита от деления на ноль
        return 0
    return abs(a * b) / gcd(a, b)

print('Наибольший общий делитель: ', gcd(10, -5))
print('Наименьшее общее кратное: ', lcm(10, -5))