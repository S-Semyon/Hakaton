from threading import Thread
from typing import Callable


class Event:
    """Обработчик ивентов"""

    def __init__(self):
        self.__need_press_key__queue: list[Callable[[str], ...]] = []

    def need_press_key(self, key: str):
        for func in self.__need_press_key__queue:
            th = Thread(target=func, args=(key, ))
            th.start()
