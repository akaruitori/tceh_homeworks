import math


"""
Задача: написать класс, который выводит сумму купленных продуктов

Продукты (у каждого есть цена):
- на вес
- за штуку
- за объем

2: напечать размерность при вычислении
300$ за 4000кг
20$ за 2штуки
10$ за 1литр

3: делать скидку на продукты (5%) при покупке более 2 товараов одного
вида поштучно

4: при покупке за граммы округлять до 50г
"""


class Product(object):
    def __init__(self, label, price, amount, measure):
        """
        Атрибуты каждого товара: название (str), цена(float),
        приобретённое количествово (float) и мера (str) товара.
        """
        self.label = label
        self.price = price
        self.amount = amount
        self.measure = measure

    def get_cost(self):
        """
        Возвращает стоимость продукта, округляя до копеек.
        """
        return round(self.price * self.amount, 2)

    def __str__(self):
        """
        Возвращает строку товара в чеке.
        """
        return '{} {} {} ..... {} руб.'.format(
            self.label, self.amount, self.measure, self.get_cost())


class SoldByItems(Product):
    def get_cost(self):
        """
        Возвращает стоимость поштучных товаров, применяет скидку,
        если кол-во > 2.
        """
        if self.amount > 2:
            return round(super().get_cost() * .95, 2)
        return super().get_cost()


class SoldByWeight(Product):
    def __init__(self, label, price, amount, measure):
        """
        Округляет кол-во весового продукта до кратности 0,05
        """
        Product.__init__(self, label, price, amount, measure)
        self.amount = math.ceil((amount - 0.024) * 20) / 20
        # math.ceil(x * 20) / 20 возвращает число x, округленное вверх
        # до кратности 0,05. Поправка на -0.024 нужна, чтобы округление
        # стало математическим: 0.124 -> 0.1, 0.125 -> 0.15


class CashDeck(object):
    def get_total_cost(self, basket):
        """
        basket: список с элементами класса Product
        Возвращает стоимость товаров в корзине.
        """
        total_cost = 0
        for item in basket:
            total_cost += item.get_cost()
        return round(total_cost, 2)

    def print_invoice(self, basket):
        """
        Печатает список товаров из basket и их общую стоимость
        """
        print('Список покупок:')
        for item in basket:
            print(item)
        print('Итого: {} руб.'.format(self.get_total_cost(basket)))


basket = [SoldByWeight('Апельсины', 85.15, 3.226, 'кг'),
          SoldByWeight('Помидоры', 105.90, 0.675, 'кг'),
          SoldByWeight('Конфеты', 554.95, 0.324, 'кг'),
          SoldByItems('Тетрадь', 15.30, 5, 'шт.'),
          SoldByItems('Шоколад', 69.99, 1, 'шт.'),
          Product('Молоко', 85.30, 1.5, 'л'),
          Product('Растительное масло', 127.50, 0.5, 'л')]

cash_deck_25 = CashDeck()

if __name__ == '__main__':

    cash_deck_25.print_invoice(basket)
