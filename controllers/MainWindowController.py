import sys
import threading

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon, QMainWindow

from MainWindows import Ui_MainWindow
import time

from settingsWindow import Ui_Dialog


class MainWindowController():
    def __init__(self,window:QMainWindow,ui:Ui_MainWindow,time_to_start_long_break:int,time_for_long_break:int,time_for_short_break:int,time_to_start_short_break:int) -> None:
        super().__init__()
        self.windows=window
        self.ui=ui
        self.time_for_long_break=time_for_long_break
        ui.end.clicked.connect(self.close)
        ui.btnStartWork.clicked.connect(self.startWorks)
        self.add_tray_menu()
        self.time_for_short_break=time_for_short_break
        self.time_to_start_short_break=time_to_start_short_break
        self.time_to_end_break=0
        self.time_to_start_long_break=time_to_start_long_break
        self.long_break_start_time=time.time()
        self.is_short_break=False



    def close(self):
        self.windows.close()

    def startWorks(self):
        self.windows.hide()
        self.long = threading.Timer(self.time_to_start_long_break,self.make_long_break)


        if(not(self.is_short_break)):
            self.long_break_start_time = time.time()
            self.long.start()
        if (self.is_enough_time_for_short()):
            self.start_short_interval()

    def start_short_interval(self):
        self.short = threading.Timer(self.time_to_start_short_break, self.make_short_break)
        self.short.start()

    def make_short_break(self):
        self.time_to_end_break=self.time_for_short_break
        self.windows.show()
        self.is_short_break=True
        self.update_time_label()
        threading.Timer(1,self.break_step).start()
    def break_step(self):
        self.time_to_end_break-=1
        self.update_time_label()
        if self.time_to_end_break>0:
            threading.Timer(1, self.break_step).start()
    def update_time_label(self):
        if self.time_to_end_break>0:
            self.ui.labInfo.setText("Czas do zakończenia przerwy:" + str(self.time_to_end_break))
        else:
            self.ui.labInfo.setText("Możesz rozpocząć pracę!")
    def make_long_break(self):
        self.time_to_end_break = self.time_for_long_break
        self.windows.show()
        self.is_short_break = False
        self.update_time_label()
        threading.Timer(1, self.break_step).start()

    def add_tray_menu(self):
        icon = QIcon("ikona.png")
        menu = QMenu()
        exitAction = menu.addAction("Ustawienia")
        exitAction.triggered.connect(self.open_settigns)

        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(sys.exit)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)

        self.tray.show()
    def open_settigns(self):
        window = QtWidgets.QDialog()

        ui_settings=Ui_Dialog()
        ui_settings.setupUi(window)
        self.init_settings_values(ui_settings)
        if(window.exec_()):

            self.time_for_long_break=ui_settings.spin_time_for_long_break.value()*60
            self.time_for_short_break=ui_settings.spin_shor_break_time.value()
            self.time_to_start_long_break=ui_settings.spin_time_to_long_break.value()*60
            self.time_to_start_short_break=ui_settings.spin_time_to_short_break.value()*60

    def init_settings_values(self,ui_settings:Ui_Dialog):

        ui_settings.spin_time_for_long_break.setValue(self.time_for_long_break/60)
        ui_settings.spin_shor_break_time.setValue(self.time_for_short_break)
        ui_settings.spin_time_to_long_break.setValue(self.time_to_start_long_break/60)

        ui_settings.spin_time_to_short_break.setValue(self.time_to_start_short_break/60)
    def is_enough_time_for_short(self):
        time_form_last_long_break=time.time()-self.long_break_start_time
        return (self.time_to_start_long_break-time_form_last_long_break)-self.time_to_start_short_break-self.time_for_short_break>0




