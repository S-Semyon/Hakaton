import random

from pynput.keyboard import Listener

from libs.events import Event

var_list = (
    ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
    ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'),
    ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'),
    ('z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/')
)


class Twister:
    def __init__(self, event: Event):
        self.event = event
        self.l_key = []
        self.over = False
        self.l_range = []
        self.x = None
        self.y = None
        self.key_last = ''
        self.released = []

        self._listener = Listener(
            on_press=self.on_press_f,
            on_release=self.on_release_f
        )

    def start(self):
        print("Твистер запущен")
        self._listener.start()

    def stop(self):
        self._listener.stop()

    def randomize_key(self):
        y = random.randint(0, 3)
        op = random.randint(0, 1)
        st = self.l_range[random.randint(0, len(self.l_range) - 1)]
        dep_x = random.randint(1, 2)

        if op == 0:
            x = st - dep_x
            if x < 0:
                x = 0
        else:
            x = st + dep_x
            if (y == 0 or y == 1) and x > 11:
                x = x - 4
            if (y == 2 or y == 3) and x > 9:
                x = x - 4

        return x, y

    def on_release_f(self, key):

        if not hasattr(key, "char"):
            return

        if key.char in self.released:
            print(key.char, "is up")
            self.released.remove(key.char)
        if self.key_last != key.char:
            self.over = True
            self.event.game_over()
            self.stop()

    def on_press_f(self, key):

        if not hasattr(key, "char"):
            return

        if key.char not in self.released:
            print(key.char, "released")
            self.released.append(key.char)

        s_x = None
        s_y = None

        for i in range(4):
            if key.char in var_list[i]:
                s_x = var_list[i].index(key.char)
                s_y = i

        if ((self.x is None) and (self.y is None)) or ((self.x == s_x) and (self.y == s_y)):
            if key.char not in self.l_key:
                self.l_key.append(key.char)
            for i in range(4):
                if key.char in var_list[i]:
                    if var_list[i].index(key.char) not in self.l_range:
                        self.l_range.append(var_list[i].index(key.char))

            if len(self.l_key) == 3:
                self.key_last = self.l_key[0]
                self.l_key.pop(0)
                self.l_range.pop(0)

            rand_x, rand_y = self.randomize_key()
            while rand_x == self.x and rand_y == self.y:
                rand_x, rand_y = self.randomize_key()

            self.x = rand_x
            self.y = rand_y

            self.event.need_release_key(self.key_last)
            self.event.need_press_key(var_list[self.y][self.x])
