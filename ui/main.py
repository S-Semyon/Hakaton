from PyQt5.QtWidgets import QMainWindow

from libs.config import UserStatistic
from ._ui.main import Ui_MainWindow


class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_statistic()
        self.modes.clicked.connect(
            lambda: self.tabWidget.setCurrentIndex(1)
        )
        self.statistics.clicked.connect(
            lambda: self.tabWidget.setCurrentIndex(2)
        )

        for btn in (self.back, self.back_2, self.back_3):
            btn.clicked.connect(
                lambda: self.tabWidget.setCurrentIndex(0)
            )

    def update_statistic(self):
        udata = UserStatistic()
        self.clicks.setText(f"Количество кликов: {udata.clicks}")
        self.errors.setText(f"Количество ошибок: {udata.errors}")
