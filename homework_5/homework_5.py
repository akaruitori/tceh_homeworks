import collections
import random


"""
1. Написать списковые выражения, которые:

создают список из строк всех нечетных чисел от 1 до 100
"""
problem_1_1 = [str(i) for i in range(1, 101, 2)]


"""
создают список из объектов другого списка, кроме итерируемых
"""
other_list = [123, 'abc', [1, 3, 7], True, {1: 'a', 2: 'b'}, {1, 2, 3}, 2.345]
problem_1_2 = [i for i in other_list if isinstance(i, collections.Iterable)]


"""
создают список из фразы 'The quick brown fox jumps over the lazy dog',
где каждый объект списка - кортеж из: слова в верхнем регистре,
слова в случанйном регистре (qUIcK) и длины слова
"""
sentence = 'The quick brown fox jumps over the lazy dog'
problem_1_3 = [(word.upper(),
                ''.join(random.choice([letter.upper(), letter.lower()])
                        for letter in word),
                len(word))
               for word in sentence.split(sep=' ')]


"""
2. Написать класс IntToStr, у которого есть одно поле: value.
А тип поля - число. Его задачей должно быть реализация возможности
сложения чисел и строк. Примеры:
obj = IntToStr(9.2)
print(obj + 3)  # 12.2
print('a' + obj)  # a9.2
print(obj + 'z')  # 9.2z
"""


class IntToStr(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, some_var):
        """
        some_var: int, float, str
        Добавляет возможность складывать IntToStr со строкой
        """
        if isinstance(some_var, str):
            return str(self.value) + some_var
        return self.value + some_var

    def __radd__(self, some_var):
        """
        some_var: int, float, str
        Добавляет возможность складывать строку с IntToStr
        """
        if isinstance(some_var, str):
            return some_var + str(self.value)
        return some_var + self.value


"""
3. Написать класс Stack, у которого есть два метода push(value)
и pop(). Если мы пытаемся сделать pop из пустого стека, нужно
выбрасывать исключение IndexError.
"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        value: любой объект
        Добавляет в стек value, выводит сообщение
        """
        self.stack.append(value)
        print('Item "{}" added.'.format(value))

    def pop(self):
        """
        Удаляет крайний элемент стека, выводит сообщение
        Если стек пустой, рождает исключение IndexError
        """
        print('Item "{}" removed.'.format(self.stack.pop()))


if __name__ == '__main__':

    print('Problem 1:\n{}\n{}\n{}\n'.format(
        problem_1_1, problem_1_2, problem_1_3))

    print('\nProblem 2:')
    a = IntToStr(12.234)

    print('IntToStr + 25.34 =', a + 25.34)
    print('25 + IntToStr =', 25 + a)
    print('"abc" + IntToStr =', 'abc' + a)
    print('IntToStr + "abc" =', a + 'abc')

    print('\nProblem 3:')
    try:
        stack = Stack()
        stack.push('abc')
        stack.push([12, 15, 18])
        stack.pop()
        stack.pop()
        stack.pop()
    except IndexError:
        print('Error, stack is empty.')
