from main_window import MainWindow
from PySide2.QtWidgets import *

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
