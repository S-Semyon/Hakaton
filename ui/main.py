from PyQt5.QtWidgets import QMainWindow

from libs.config import UserStatistic
from libs.events import Event
from libs.timer import Timer
from libs.twister import Twister
from ._ui.main import Ui_MainWindow


class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_statistic()
        self.event = Event()

        self.event.add_func_press_key(
            lambda key: self.need_click.setText(f"Нажмите {key}")
        )
        self.event.add_func_release_key(
            lambda key: self.need_release.setText(f"Отожмите {key}")
        )
        self.event.add_func_game_over(
            self.game_over
        )

        self.twister = Twister(self.event)
        self.timer = Timer(self.text_timer)

        self.modes.clicked.connect(
            lambda: self.tabWidget.setCurrentIndex(1)
        )
        self.statistics.clicked.connect(
            lambda: self.tabWidget.setCurrentIndex(2)
        )
        self.btn_game.clicked.connect(
            self.new_game
        )
        self.btn_time_game.clicked.connect(
            self.new_time_game
        )

        for btn in (self.back, self.back_2, self.back_3):
            btn.clicked.connect(
                lambda: self.tabWidget.setCurrentIndex(0)
            )

    def update_statistic(self):
        udata = UserStatistic()
        self.clicks.setText(f"Количество кликов: {udata.clicks}")
        self.errors.setText(f"Количество ошибок: {udata.errors}")

    def new_game(self):
        self.tabWidget.setCurrentIndex(3)
        self.text_timer.setText("")
        self.twister.start()

    def new_time_game(self):
        self.tabWidget.setCurrentIndex(3)
        self.timer.start_timer()
        self.twister.start()

    def game_over(self):
        self.twister.stop()
        self.tabWidget.setCurrentIndex(4)
        self.update_statistic()
