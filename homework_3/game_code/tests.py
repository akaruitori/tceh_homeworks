# -*- coding: utf-8 -*-

from __future__ import print_function

import inspect
import sys
import contextlib

import game
from game import (
    shuffle_field,
    is_game_finished,
    handle_user_input,
    perform_move,
    EMPTY_MARK,
)

__author__ = 'sobolevn'


class AssertionTestException(AssertionError):
    pass


class BaseTestClass(object):
    fails = 0
    passed = 0

    def run_tests(self):
        print('Starting tests for: {}'.format(self.__class__.__name__))

        for method in dir(self):
            candidate = getattr(self, method)
            if callable(candidate) and method.startswith('test_'):
                try:
                    candidate()
                    self.__class__.passed += 1
                except AssertionTestException as ex:
                    print('{} failed: '.format(method), ex)
                    self.__class__.fails += 1

        fails = self.__class__.fails
        all_tests = fails + self.__class__.passed
        print("Finished class' tests: {}/{}".format(
                (all_tests - fails), all_tests))
        print()

    def _assert_compare(self, first, second, equality=True):
        if (first == second) != equality:
            message = 'does not equal' if equality else 'equals'
            raise AssertionTestException('{}.{}: {} {} {}'.format(
                    self.__class__.__name__,
                    inspect.stack()[1][3],
                    first,
                    message,
                    second,
            ))

    def assert_equal(self, first, second):
        self._assert_compare(first, second, equality=True)

    def assert_not_equal(self, first, second):
        self._assert_compare(first, second, equality=False)

    @contextlib.contextmanager
    def assert_raises(self, exception):
        try:
            yield
            raise AssertionTestException('{}.{}: does not rise {}'.format(
                    self.__class__.__name__,
                    inspect.stack()[1][3],
                    exception,
            ))
        except exception:
            pass


class TestShuffleField(BaseTestClass):
    def test_length(self):
        result = shuffle_field()
        self.assert_equal(len(result), 16)

    def test_randomness(self):
        result1 = shuffle_field()
        result2 = shuffle_field()
        self.assert_not_equal(result1, result2)

    def test_type(self):
        result = shuffle_field()
        self.assert_equal(isinstance(result, list), True)


class TestIsGameFinished(BaseTestClass):
    def test_finished_state(self):
        finished_state = list(range(1, 16))
        finished_state.append(EMPTY_MARK)

        result = is_game_finished(finished_state)
        self.assert_equal(result, True)

    def test_unfinished_states(self):
        unfinished_state = list(range(1, 16))
        unfinished_state.append(EMPTY_MARK)
        unfinished_state[0], unfinished_state[-1] = \
            unfinished_state[-1], unfinished_state[0]

        result = is_game_finished(unfinished_state)
        self.assert_equal(result, False)


class TestUserInput(BaseTestClass):
    @contextlib.contextmanager
    def _patch_user_input(self, obj, value):
        if sys.version_info[0] == 3:
            obj.input = lambda _: value
        else:
            obj.raw_input = lambda _: value

        yield

        # setting values back just in case:
        if sys.version_info[0] == 3:
            obj.input = input
        else:
            obj.raw_input = raw_input

    def test_right_input(self):
        with self._patch_user_input(game, 'w'):
            move = handle_user_input()
        self.assert_equal(move, 'w')


class TestPerformMove(BaseTestClass):
    left_down_corner_index = 12
    right_up_corner_index = 3

    @classmethod
    def _left_down_corner(cls):
        state = list(range(15))
        state[0], state[1] = state[1], state[0]
        state.insert(cls.left_down_corner_index, EMPTY_MARK)
        return state

    @classmethod
    def _right_up_corner(cls):
        state = cls._left_down_corner()
        state[cls.left_down_corner_index], state[cls.right_up_corner_index] = \
            state[cls.right_up_corner_index], state[cls.left_down_corner_index]
        return state

    def test_up_move(self):
        state = self._left_down_corner()
        result = perform_move(state, 'w')

        result_index = result.index(EMPTY_MARK)
        self.assert_equal(result_index, self.left_down_corner_index - 4)

    def test_right_move(self):
        state = self._left_down_corner()
        result = perform_move(state, 'd')

        result_index = result.index(EMPTY_MARK)
        self.assert_equal(result_index, self.left_down_corner_index + 1)

    def test_left_move(self):
        state = self._right_up_corner()
        result = perform_move(state, 'a')

        result_index = result.index(EMPTY_MARK)
        self.assert_equal(result_index, self.right_up_corner_index - 1)

    def test_down_move(self):
        state = self._right_up_corner()
        result = perform_move(state, 's')

        result_index = result.index(EMPTY_MARK)
        self.assert_equal(result_index, self.right_up_corner_index + 4)

    def test_bad_moves(self):
        state = self._right_up_corner()
        with self.assert_raises(IndexError):
            perform_move(state, 'w')

        with self.assert_raises(IndexError):
            perform_move(state, 'd')

        state = self._left_down_corner()
        with self.assert_raises(IndexError):
            perform_move(state, 'a')

        with self.assert_raises(IndexError):
            perform_move(state, 's')


if __name__ == '__main__':
    all_passed = 0
    all_fails = 0

    # Detect tests:
    for name, klass in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(klass) and issubclass(klass, BaseTestClass) \
                and klass is not BaseTestClass:
            klass().run_tests()
            all_passed += klass.passed
            all_fails += klass.fails

    print('Total fails: {}'.format(all_fails))