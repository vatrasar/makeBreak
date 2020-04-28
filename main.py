import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon, QApplication

from MainWindowController import MainWindowController
from MainWindows import Ui_MainWindow








if __name__ == "__main__":
    app2 = QApplication(sys.argv)

    window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)
    controller = MainWindowController(window,ui,20,20,5,5)
    window.show()
    sys.exit(app2.exec_())
