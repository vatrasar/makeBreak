import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from controllers.MainWindowController import MainWindowController
from MainWindows import Ui_MainWindow








if __name__ == "__main__":
    app2 = QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    app2.setWindowIcon(QIcon("resources/ikona.png"))
    ui = Ui_MainWindow()
    ui.setupUi(window)
    controller = MainWindowController(window,ui,3600,180,20,1200)
    window.show()
    sys.exit(app2.exec_())
