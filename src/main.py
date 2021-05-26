from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from main_window import MainWindow
from ui.splash_screen.ui_splash_screen import Ui_SplashScreen

import platform
import sys

counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTimer start (milliseconds)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(60)

        # Change texts
        self.ui.labelDescription.setText("<strong>LOADING</strong> RESOURCES")
        QtCore.QTimer.singleShot(
            2000,
            lambda: self.ui.labelDescription.setText(
                "<strong>LOADING</strong> SCRIPTS"
            ),
        )
        QtCore.QTimer.singleShot(
            3500,
            lambda: self.ui.labelDescription.setText(
                "<strong>LOADING</strong> DATABASE"
            ),
        )
        QtCore.QTimer.singleShot(
            5000,
            lambda: self.ui.labelDescription.setText(
                "<strong>LOADING</strong> USER INTERFACE"
            ),
        )

        self.show()

    def setup_ui(self):
        # Since there were some conflicts between icons,
        # the three following lines bypass the issue.
        import ctypes
        my_app_id = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
        
        self.setWindowIcon(QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Analytics | Loading...", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        # Close splash screen and start the application
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
