import sys
import threading

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon, QMainWindow, QAction

from MainWindows import Ui_MainWindow
import time

from settingsWindow import Ui_Dialog


class MainWindowController():
    def __init__(self,window:QMainWindow,ui:Ui_MainWindow,time_to_start_long_break:int,time_for_long_break:int,time_for_short_break:int,time_to_start_short_break:int) -> None:
        super().__init__()
        self.windows=window
        self.ui=ui
        self.time_for_long_break=time_for_long_break

        ui.btnStartWork.clicked.connect(self.startWorks)
        self.add_tray_menu()
        self.time_for_short_break=time_for_short_break
        self.time_to_start_short_break=time_to_start_short_break
        self.time_to_end_break=0
        self.time_to_start_long_break=time_to_start_long_break
        self.long_break_start_time=time.time()
        self.is_short_break=False
        self.load_conf_from_file()



    def close(self):
        self.windows.close()

    def startWorks(self):
        self.windows.hide()
        self.longThread = threading.Timer(self.time_to_start_long_break,self.make_long_break)


        if(not(self.is_short_break)):
            self.long_break_start_time = time.time()
            self.longThread.start()
        if (self.is_enough_time_for_short()):
            self.start_short_interval()

    def start_short_interval(self):
        self.shortThread = threading.Timer(self.time_to_start_short_break, self.make_short_break)
        self.shortThread.start()

    def make_short_break(self):
        self.ui.btnStartWork.setEnabled(False)
        self.time_to_end_break=self.time_for_short_break
        self.windows.showFullScreen()
        self.is_short_break=True
        self.update_time_label()
        threading.Timer(1,self.break_step).start()


    def break_step(self):
        self.time_to_end_break-=1
        self.update_time_label()
        if self.time_to_end_break>0:
            threading.Timer(1, self.break_step).start()
        else:
            self.ui.btnStartWork.setEnabled(True)


    def update_time_label(self):
        if self.time_to_end_break>0:
            self.ui.labInfo.setText("Czas do zakończenia przerwy:" + str(self.time_to_end_break))
        else:
            self.ui.labInfo.setText("Możesz rozpocząć pracę!")
    def make_long_break(self):
        self.ui.btnStartWork.setEnabled(False)
        self.time_to_end_break = self.time_for_long_break
        self.windows.showFullScreen()
        self.is_short_break = False
        self.update_time_label()
        threading.Timer(1, self.break_step).start()

    def add_tray_menu(self):
        icon = QIcon("ikona.png")
        menu = QMenu()


        settingsAction = menu.addAction("Ustawienia")
        settingsAction.triggered.connect(self.open_settigns)

        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(self.exit)



        self.stopAction = menu.addAction("Zatrzymaj")
        self.stopAction.triggered.connect(self.disable_breaks)


        self.resumeAction = menu.addAction("Wznów")
        self.resumeAction.triggered.connect(self.reasum_breaks)
        self.resumeAction.setEnabled(False)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)

        self.tray.show()
    def exit(self):
        self.shortThread.cancel()
        self.longThread.cancel()
        sys.exit()
    def reasum_breaks(self):
        self.startWorks()
        self.stopAction.setEnabled(True)
        self.resumeAction.setEnabled(False)
    def disable_breaks(self):
        self.shortThread.cancel()
        self.longThread.cancel()
        self.stopAction.setEnabled(False)
        self.resumeAction.setEnabled(True)
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
            self.save_conf_to_file()



    def init_settings_values(self,ui_settings:Ui_Dialog):

        ui_settings.spin_time_for_long_break.setValue(self.time_for_long_break/60)
        ui_settings.spin_shor_break_time.setValue(self.time_for_short_break)
        ui_settings.spin_time_to_long_break.setValue(self.time_to_start_long_break/60)

        ui_settings.spin_time_to_short_break.setValue(self.time_to_start_short_break/60)
    def is_enough_time_for_short(self):
        time_form_last_long_break=time.time()-self.long_break_start_time
        return (self.time_to_start_long_break-time_form_last_long_break)-self.time_to_start_short_break-self.time_for_short_break>0

    def load_conf_from_file(self):
        file_in=open("conf.txt","r")
        self.time_for_long_break=int(file_in.readline())
        self.time_for_short_break=int(file_in.readline())
        self.time_to_start_long_break=int(file_in.readline())
        self.time_to_start_short_break=int(file_in.readline())
        file_in.close()

    def save_conf_to_file(self):
        file_out = open("conf.txt", "w")
        file_out.write(str(self.time_for_long_break)+"\n")
        file_out.write(str(self.time_for_short_break)+"\n")
        file_out.write(str(self.time_to_start_long_break)+"\n")
        file_out.write(str(self.time_to_start_short_break)+"\n")
        file_out.close()


