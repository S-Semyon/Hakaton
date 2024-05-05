from threading import Thread
from typing import Callable

from libs.config import UserStatistic


class Event:
    """Обработчик ивентов"""

    def __init__(self):
        self.UserStatistic = UserStatistic()
        self.__need_press_key__queue: list[Callable[[str], ...]] = []
        self.__need_release_key__queue: list[Callable[[str], ...]] = []
        self.__game_over__queue: list[Callable[..., ...]] = []

    def add_func_press_key(self, func: Callable[[str], ...]):
        """Добавить функцию для ивента 'клавишу нужно зажать'"""
        self.__need_press_key__queue.append(func)

    def add_func_release_key(self, func: Callable[[str], ...]):
        """Добавить функцию для ивента 'клавишу нужно отжать'"""
        self.__need_release_key__queue.append(func)

    def add_func_game_over(self, func: Callable[..., ...]):
        """Добавить функцию для ивента 'проигрыш'"""
        self.__game_over__queue.append(func)

    def need_press_key(self, key: str):
        """Вызвать ивент 'клавишу нужно зажать'"""
        self.UserStatistic.clicks += 1
        for func in self.__need_press_key__queue:
            th = Thread(target=func, args=(key, ))
            th.start()

    def need_release_key(self, key: str):
        """Вызвать ивент 'клавиша нужно отжать'"""
        for func in self.__need_release_key__queue:
            th = Thread(target=func, args=(key, ))
            th.start()

    def game_over(self):
        """Вызвать ивент 'проигрыш'"""
        self.UserStatistic.errors += 1
        for func in self.__game_over__queue:
            th = Thread(target=func)
            th.start()
