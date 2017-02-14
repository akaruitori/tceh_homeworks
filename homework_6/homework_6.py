from timeit import default_timer
from math import pow
from random import random
from datetime import date, timedelta


"""
1. Написать декоратор, который отменяет выполнение функции и пишет:
ИМЯ_ФУНКЦИИ не будет вызвана
"""


def cancel_execution(func):
    def wrapper(*args):
        print('Функция {} не будет вызвана'.format(func.__name__))
    return wrapper


@cancel_execution
def power(a, b):
    return pow(a, b)


"""
2. Реализовать декоратор, который измеряет скорость выполнения функций.
Написать три разные функции, задекорировать их и проверить.
"""

# Устроим соревнование по скорости между тремя реализованными
# разными способами функциями, возводящими число в степень.


def time_it(func):
    """
    Декоратор. Запускает функцию 10 000 раз и выводит время выполнения.
    """
    def measure_time(a, b):
        start = default_timer()

        for _ in range(10000):
            func(a, b)

        end = default_timer()
        print('{} took {} seconds.'.format(func.__name__,
                                           round(end - start, 3)))
    return measure_time


@time_it
def power_via_iteration(a, b):
    result = a
    while b > 1:
        result *= a
        b -= 1
    return result


@time_it
def power_via_recursion(a, b):
    # Чтобы декорировать рекурсивную функцию, пришлось её сделать
    # вложенной. Ничего более элегантного я не придумала :(
    def power(a, b):
        if b == 1:
            return a
        return power(a, (b - 1))
    return power(a, b)


@time_it
def power_via_math(a, b):
    return pow(a, b)


"""
3. Написать генероторное выражение, которое включает в себя все четные
числа от 0 до 100.
"""

even_number = (m for m in range(0, 100, 2))


"""
4. Написать генератор, который возвращает бесконечную последовательность
случайных чисел, таких что следующее не меньше прошлого.
"""


def generate_rand_num(n):
    while True:
        n += random() * 100
        yield round(n, 2)


"""
5. Написать генератор, который принимает на вход дату и на каждый вызов
выдает следующий день.
"""


def generate_next_day(some_date):
    """
    some_date: объект класса datetime.date()
    """
    while True:
        some_date += timedelta(days=1)
        yield some_date.strftime('%A, %d of %B %Y')


"""
Тесты.
"""
if __name__ == '__main__':
    print('Задача 1:')
    power(2, 5)

    print('\nЗадача 2:')
    power_via_iteration(2, 950)
    power_via_recursion(2, 950)
    power_via_math(2, 950)

    print('\nЗадача 3:')
    for _ in range(50):
        print(next(even_number), end=' ')

    print('\n\nЗадача 4:')
    n = generate_rand_num(0)
    for _ in range(20):
        print(next(n), end=' ')

    print('\n\nЗадача 5:')
    a = generate_next_day(date.today())
    for _ in range(5):
        print(next(a))
