# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from HOMEACCOUNT_UIC import Ui_MainWindow
from res.DLL_CLASS_COMM import dt_day, dt_month, dt_year, convert_month
from COUNTERS_END import Counters
# from END_KommPlateg import KommunalPlateg
# from END_DebitKredit import DebitKredit


# ОСНОВНОЕ ОКНО ПРОГРАММЫ
class KOMUNAL(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KOMUNAL, self).__init__(parent)
        self.PokazSchet = Counters()
        # self.KommunalPlateg = KommunalPlateg()
        # self.DebitKredit = DebitKredit()

        self.setupUi(self)

        # показывает текущую дату
        self.label_month_year.setText(dt_day + " " + convert_month(dt_month) + " " + dt_year)

        self.action_PokazSchet.triggered.connect(self.open_ps)  # вызывает окно ПОКАЗАНИЯ СЧЕТЧИКОВ
        self.action_KomunPlateg.triggered.connect(self.open_kp)  # вызывает окно КОМУНАЛЬНЫЕ ПЛАТЕЖИ
        self.action_DebitKredit.triggered.connect(self.open_db)  # вызывает окно ДОХОДЫ/РАСХОДЫ

        self.action_Exit.triggered.connect(self.close_main)  # закрывает окно KOMMUNAL

    def open_ps(self):  # открывает окно ПОКАЗАНИЯ СЧЕТЧИКОВ
        self.PokazSchet.show()

    def open_kp(self):  # открывает окно КОМУНАЛЬНЫЕ ПЛАТЕЖИ
        self.KommunalPlateg.show()

    def open_db(self):  # открывает окно ДОХОДЫ/РАСХОДЫ
        self.DebitKredit.show()

    def close_main(self):  # закрывает окно KOMMUNAL
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle("Fusion")
    window = KOMUNAL()
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение
