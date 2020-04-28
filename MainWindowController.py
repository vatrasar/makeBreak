import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon

from MainWindows import Ui_MainWindow


class MainWindowController():
    def __init__(self,window) -> None:
        super().__init__()
        self.windows=window

        # ui.end.clicked.connect(self.close)
        self.add_tray_menu()

    # def close(self):
    #     self.windows.close()

    def add_tray_menu(self):
        icon = QIcon("ikona.png")
        menu = QMenu()

        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(sys.exit)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)

        self.tray.show()




