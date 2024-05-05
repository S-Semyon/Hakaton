#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main import Ui

__VERSION__ = (0, 1, 0)


def main():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
