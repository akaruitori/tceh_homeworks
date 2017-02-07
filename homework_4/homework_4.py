"""
Реализовать класс Person, у которого должно быть два публичных поля: age и name.
Также у него должен быть следующий набор методов: know(person), который позволяет добавить другого человека
в список знакомых. И метод is_known(person), который возвращает знает ли знакомы ли два человека
"""

class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.known_people =[]

    def know(self, other_person):
        self.known_people.append(other_person)

    def is_known(self, other_person):
        return other_person in self.known_people

jack = Person('Jack', 25)
alice = Person('Alice', 24)

print("Does {} ever met {}?".format(jack.name, alice.name),jack.is_known(alice))
jack.know(alice)
print("Does {} ever met {}?".format(jack.name, alice.name),jack.is_known(alice))


"""
Есть класс, который выводит информацию в консоль: `Printer`, у него есть метод: log(*values).
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
"""
class Printer(object):

    def log(self, *values):
        return str(values)

class FormattedPrinter(Printer):

    def log_with_stars(self, *values):
        # Если Printer.log(*values) возвращает строковое значение:
        print('***\n' + self.log(*values) + '\n***')



a = Printer()
b = FormattedPrinter()

print()
print(a.log(25, 'a', 34.2, [25, 34], True))
print()
b.log_with_stars(25, 'a', 34.2, [25, 34], True)


"""
Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""

class Animal(object):
    # Задаю три атрибута как критерии опасности для человека:
    # size: оценочный размер, int, от 0 (крошечное) до 9 (огромное)
    # is_predator: принадлежность к хищникам, True или False
    # is_poisonous: ядовито ли животное для человека, True или False
    def __init__(self, kind, size, is_predator, is_poisonous = False):
        self.kind = kind
        self.size = size
        self.is_predator = is_predator
        self.is_poisonous = is_poisonous


class Human(object):
    def __init__(self, name):
        self.name = name

    def is_dangerous(self, animal):
        # Грубо принимаю, что маленькие (size 0-3) хищники опасности не представляют,
        # ядовитые животные опасны при любом размере.
        if animal.is_predator and animal.size > 3:
            return True
        return animal.is_poisonous


kate = Human('Kate')
fluffy = Animal('Dog', size = 3, is_predator = True)
balu = Animal('Bear', size = 7, is_predator = True)
cute_spider = Animal('Poisonous Spider', size = 0, is_predator = True, is_poisonous = True)
spirit = Animal('Horse', size = 6, is_predator = False)

print()
print('Is {} dangerous for {}?'.format(fluffy.kind, kate.name), kate.is_dangerous(fluffy))
print('Is {} dangerous for {}?'.format(balu.kind, kate.name), kate.is_dangerous(balu))
print('Is {} dangerous for {}?'.format(cute_spider.kind, kate.name), kate.is_dangerous(cute_spider))
print('Is {} dangerous for {}?'.format(spirit.kind, kate.name), kate.is_dangerous(spirit))
