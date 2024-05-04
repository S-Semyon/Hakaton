#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui._ui.main import UiMainWindow

__VERSION__ = (0, 0, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UiMainWindow(QMainWindow())
    window.MainWindow.show()

    sys.exit(app.exec_())
