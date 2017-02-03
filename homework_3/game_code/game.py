# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    def is_solvable(field):
        """
        Принимает перемешанное поле field. Возвращает True, если головоломка на этом поле решаема (N -- четное число),
        или False в противном случае.
        """
        mark_pos = field.index(0)

        # Начальное значение N -- номер ряда с пустой клеткой.
        N = mark_pos // 4 + 1

        # Считает для каждого элемента (кроме 0 и 1) кол-во последующих меньшего значения (кроме 0). Всё суммирует в N.
        for i in range(15):
            if 0 != field[i] != 1:
                for j in range(i + 1, 16):
                    if field[j] != 0 and field[i] > field[j]:
                        N += 1
        return N % 2 == 0


    field = list(range(16))
    random.shuffle(field)

    if not is_solvable(field):
        # Нерешаемое поле станет решаемым, если поменять два непустых элемента местами. Это изменит значение N на 1.
        if field[1] != 0 != field[2]:
            field[1], field[2] = field[2], field[1]
        else:
            field[14], field[15] = field[15], field[14]


    field[field.index(0)] = EMPTY_MARK
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """

    for i in range(16):
        if i % 4 == 0:
            print()

        # Добавляет пробел, если значение элемента < 10, чтобы все клетки были равной ширины:
        if field[i] == EMPTY_MARK or field[i] < 10:
            print('[ {}]'.format(field[i]), end='')
        else:
            print('[{}]'.format(field[i]), end='')
    print()



def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    return field[0:15] == list(range(1,16))


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    old_pos = field.index(EMPTY_MARK)
    new_pos = old_pos + MOVES[key]

    # Сравнивает номера рядов и столбцов, проверяет, что новый индекс пустой клетки >= 0.
    if (old_pos // 4 != new_pos // 4) and (old_pos % 4 != new_pos % 4) or new_pos < 0:
        raise IndexError

    field[old_pos], field[new_pos] = field[new_pos], field[old_pos]
    return field



def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """

    move = input('Ваш ход:\n')
    while move not in MOVES.keys():
        move = input('Сделайте ход одной из клавиш:{}\n'.format(tuple(MOVES.keys())))
    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    try:
        print('***\nНачинаем игру в пятнашки!\n***')
        moves = 0
        field = shuffle_field()
        while True:
            if is_game_finished(field):
                print('***\nПоздравляем, головоломка решена! Совершено ходов: {}\n***'.format(moves))
                break
            print_field(field)
            try:
                perform_move(field, handle_user_input())
                moves += 1
            except IndexError:
                print('Такой ход невозможен.')
    except KeyboardInterrupt:
        print('Shutting down')







if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
