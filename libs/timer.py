from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QTime
import time


class Timer:
    """Время работы сессии"""
    def __init__(self, label: QLabel):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time = 0
        self.start_time = None
        self.label = label

    def start_timer(self):
        """Запуск таймера"""
        self.start_time = time.perf_counter()
        self.timer.start()

    def update_timer(self):
        """Обновление таймера"""
        self.elapsed_time = time.perf_counter() - self.start_time
        self.label.setText(
            QTime().fromMSecsSinceStartOfDay(int(self.elapsed_time*1000)).toString()
        )
