from main_window import MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import *
from ui.splash_screen.ui_splash_screen import Ui_SplashScreen

from settings import *
import sys


class SplashScreen(QMainWindow):

    COUNTER = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.start_loading()
        self.show()

    def setup_user_interface(self):
        # Since there were some conflicts between icons,
        # the three following lines bypass the issue.
        import ctypes

        my_app_id = (
            "mycompany.myproduct.subproduct.version"  # This is an arbitrary string.
        )
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

        self.setWindowIcon(QIcon(f"ui/icons/{Strings.ICON}"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | Loading...", None
            )
        )

        # Remove title bar.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

    def start_loading(self):
        # QTimer start (milliseconds).
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

    def progress(self):
        self.ui.progressBar.setValue(self.COUNTER)

        # Close splash screen and start the application.
        if self.COUNTER > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        self.COUNTER += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
