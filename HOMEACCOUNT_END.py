# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from HOMEACCOUNT_UIC import Ui_MainWindow
from res.DLL_CLASS_COMM import dt_day, dt_month, dt_year, convert_month
from COUNTERS_END import Counters
from COMMPAY_END import CommunalPayment


# ОСНОВНОЕ ОКНО ПРОГРАММЫ
class HOME_ACCOUNT(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HOME_ACCOUNT, self).__init__(parent)
        self.Win_Counters = Counters()
        self.Win_Payments = CommunalPayment()

        self.setupUi(self)

        # показывает текущую дату
        self.label_month_year.setText(dt_day + " " + convert_month(dt_month) + " " + dt_year)

        self.action_Win_Counters.triggered.connect(self.open_COU)  # вызывает окно ПОКАЗАНИЯ СЧЕТЧИКОВ
        self.action_Win_Payments.triggered.connect(self.open_CPAY)  # вызывает окно КОМУНАЛЬНЫЕ ПЛАТЕЖИ
        # self.action_DebitKredit.triggered.connect(self.open_db)  # вызывает окно ДОХОДЫ/РАСХОДЫ

        self.action_Exit.triggered.connect(self.close_main)  # закрывает окно HOME_ACCOUNT

    def open_COU(self):  # открывает окно ПОКАЗАНИЯ СЧЕТЧИКОВ
        self.Win_Counters.show()

    def open_CPAY(self):  # открывает окно КОМУНАЛЬНЫЕ ПЛАТЕЖИ
        self.Win_Payments.show()

    # def open_db(self):  # открывает окно ДОХОДЫ/РАСХОДЫ
    #     self.DebitKredit.show()

    def close_main(self):  # закрывает окно HOME_ACCOUNT
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle("Fusion")
    window = HOME_ACCOUNT()
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение
