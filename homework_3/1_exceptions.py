"""
Задача 1. Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или RuntimeError
случайным образом. В месте вызова функции обрабатывать все три исключения
"""

import random

def raise_exception():
    raise random.choice([ValueError, TypeError, RuntimeError])

try:
    raise_exception()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except RuntimeError:
    print('RuntimeError')