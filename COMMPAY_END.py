# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QEvent, QTimer
from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_COMM import dt_day, dt_month, dt_year, month, convert_month, selected_period, \
    Period, Save_OR, SQLite3_Data_Base, text_convert, denomination, text_conv_to_num, str_list, payment_checked, \
    num_conv_to_text
from COMMPAY_UIC import UiWinPayment


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class CommunalPayment(QtWidgets.QWidget, UiWinPayment):
    def __init__(self):
        super(CommunalPayment, self).__init__()

        self.setupUi_PAY(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных

        self.data_multi = []
        self.status = "0 0 0 0 0 0"

        self.period_PAY = Period(self.comboBox_month_PAY, self.comboBox_year_PAY, self.label_month_year_PAY)

        # ВЫБОР ПЕРИОДА
        selected_period(self.comboBox_month_PAY, self.comboBox_year_PAY)
        self.comboBox_month_PAY.activated.connect(self.combo_box_period_sel)  # месяц
        self.comboBox_year_PAY.activated.connect(self.combo_box_period_sel)  # год

        # ТЕКУЩЕГО ПЕРИОДА
        self.current_month_index = month.index(convert_month(dt_month))  # Текущий месяц (int(0))

        # установка ТЕКУЩЕГО ПЕРИОДА
        if dt_day >= "11":
            self.label_month_year_PAY.setText(convert_month(dt_month) + " " + dt_year)  # заголовок ("Месяц Год")
            self.comboBox_month_PAY.setCurrentIndex(self.current_month_index)  # устанавливает текущий месяц ("Месяц")
            self.comboBox_year_PAY.setCurrentText(dt_year)  # устанавливает текущий год ("Год")
        else:
            self.label_month_year_PAY.setText(convert_month(int(dt_month) - 1) + " " + dt_year)
            self.comboBox_month_PAY.setCurrentIndex(self.current_month_index - 1)
            self.comboBox_year_PAY.setCurrentText(dt_year)

        self.btn_Left_PAY.clicked.connect(self.btn_period_left)  # прокрутка в лево
        self.btn_Right_PAY.clicked.connect(self.btn_period_right)  # прокрутка в право

        self.win_pole = [self.pay_power.line_edit_sum, self.pay_power.line_edit_quantity,
                         self.pay_power.line_edit_tariff,
                         self.pay_water.line_edit_sum, self.pay_water.line_edit_quantity,
                         self.pay_water.line_edit_tariff,
                         self.pay_gaz.line_edit_sum, self.pay_gaz.line_edit_quantity,
                         self.pay_gaz.line_edit_tariff,
                         self.pay_apartment.line_edit_sum,
                         self.pay_internet.line_edit_sum,
                         self.pay_phone.line_edit_sum,
                         self.pay_apartment.line_edit_minus_water, self.pay_apartment.line_edit_balance_sum,
                         self.lineEdit_result,
                         self.label_GL_V_1_PAY, self.label_GL_V_2_PAY, self.label_error_PAY]

        # подтверждение платежа
        self.btn_check_all.clicked.connect(self.check_btn_status_all)  # check_status_all

        self.pay_power.btn_check.clicked.connect(self.check_btn_status)  # check_status
        self.pay_water.btn_check.clicked.connect(self.check_btn_status)  # check_status
        self.pay_gaz.btn_check.clicked.connect(self.check_btn_status)  # check_status
        self.pay_apartment.btn_check.clicked.connect(self.check_btn_status)  # check_status
        self.pay_internet.btn_check.clicked.connect(self.check_btn_status)  # check_status
        self.pay_phone.btn_check.clicked.connect(self.check_btn_status)  # check_status

        self.pay_power.line_edit_tariff.installEventFilter(self)
        self.pay_water.line_edit_tariff.installEventFilter(self)
        self.pay_gaz.line_edit_tariff.installEventFilter(self)
        self.pay_apartment.line_edit_sum.installEventFilter(self)
        self.pay_internet.line_edit_sum.installEventFilter(self)
        self.pay_phone.line_edit_sum.installEventFilter(self)

        self.pay_apartment.line_edit_sum.selectAll()

        self.btn_Save_PAY.clicked.connect(self.btn_save_PAY)
        self.btn_Cancel_PAY.clicked.connect(self.btn_cancel_PAY)

        # ЧИТАЕМ показания из базы данных
        self.read_data_pay()

        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            pay_sum = obj

            def summa(pay):
                pay.selectAll()

            if obj == pay_sum:
                QTimer.singleShot(10, lambda: summa(pay_sum))
        return super(CommunalPayment, self).eventFilter(obj, event)

    def combo_box_period_sel(self):
        self.current_month_index = self.period_PAY.label_sel_period()
        if self.comboBox_year_PAY.currentText() == "2006":
            if self.comboBox_month_PAY.currentIndex() <= 5:
                self.comboBox_month_PAY.setCurrentIndex(5)
                self.label_month_year_PAY.setText("Июнь 2006")
                self.current_month_index = 5
        self.read_data_pay()

    def btn_period_left(self):
        self.combo_box_period_sel()
        if self.label_month_year_PAY.text() == "Июнь 2006":
            self.btn_Left_PAY.setEnabled(False)
        else:
            self.current_month_index = self.period_PAY.click_btn_left(self.current_month_index)
            self.read_data_pay()

    def btn_period_right(self):
        self.combo_box_period_sel()
        if self.label_month_year_PAY.text() != "Май 2006":
            self.btn_Left_PAY.setEnabled(True)
            self.current_month_index = self.period_PAY.click_btn_right(self.current_month_index)
            self.read_data_pay()

    def read_data_pay(self):
        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский 00000419

        file_db = open('COMMPAY_DAT.db', 'a')  # открывает файл базы данных
        file_db.close()  # закрывает файл базы данных

        table_counters = 'Counters_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы
        table_tariff = 'Tariff_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы
        table_payments = 'Payments_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы

        # заголовок атрибутов таблицы Tariff
        heading_tariff = 'id integer primary key , month_year text, ' \
                         'Tariff_PW integer, Tariff_WA integer, Tariff_GZ integer'

        # заголовок атрибутов таблицы Payments
        heading_payments = 'id integer primary key , month_year text, ' \
                           'Summa_PW integer, Summa_WA integer, Summa_GZ integer, ' \
                           'Summa_AP integer, Summa_IN integer, Summa_PH integer, Status text'

        # создает таблицу в базе данных, если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_tariff, heading_tariff)
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_payments, heading_payments)

        for i in self.win_pole:  # очищает поля окна
            i.clear()

        for i in self.list_payments:
            i.setChecked(False)

        self.status = "0 0 0 0 0 0"
        self.btn_check_all.setChecked(False)
        self.quantity = 0

        # читаем таблицу с ПОКАЗАНИЯМИ СЧЕТЧИКОВ
        read_table_counters = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_counters)

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_counters)):
            counter = read_table_counters[i]  # показания сохраненного периода

            # если есть сохраненные значения в таблице для данного периода
            current_month = month[self.comboBox_month_PAY.currentIndex()]
            if current_month in counter[1]:
                self.pay_power.line_edit_quantity.setText(str(counter[3] - counter[2]))
                self.pay_water.line_edit_quantity.setText(str((counter[5] - counter[4]) +
                                                              (counter[7] - counter[6]) +
                                                              (counter[9] - counter[8]) +
                                                              (counter[11] - counter[10])))
                self.pay_gaz.line_edit_quantity.setText(str(counter[13] - counter[12]))

            previous_month = month[self.comboBox_month_PAY.currentIndex() - 1]
            if previous_month in counter[1]:
                self.quantity = (counter[5] - counter[4]) + (counter[7] - counter[6]) + \
                                (counter[9] - counter[8]) + (counter[11] - counter[10])

        # проверят не является ли выбранный месяц январем (если да то передает таблицу за предыдущий год)
        if SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_counters) and \
                month[self.comboBox_month_PAY.currentIndex()] == "Январь":
            table_counters = 'Counters_year_' + str(int(self.comboBox_year_PAY.currentText()) - 1)

            read_table_counters = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_counters)

            counter = read_table_counters[-1]  # показания сохраненного периода
            self.quantity = (counter[5] - counter[4]) + (counter[7] - counter[6]) + \
                            (counter[9] - counter[8]) + (counter[11] - counter[10])

        # читаем таблицу с ТАРИФАМИ
        # проверят не является ли выбранный месяц январем (если да то передает таблицу за предыдущий год)
        if not SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_tariff) and \
                month[self.comboBox_month_PAY.currentIndex()] == "Январь":
            table_tariff = 'Tariff_year_' + str(int(self.comboBox_year_PAY.currentText()) - 1)

        read_table_tariff = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_tariff)

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_tariff)):
            tariff = read_table_tariff[i]  # показания сохраненного периода

            # если есть сохраненные значения (данного периода)
            current_month = month[self.comboBox_month_PAY.currentIndex()]
            if current_month in tariff[1]:
                self.pay_power.line_edit_tariff.setText(str(tariff[2]))
                self.pay_water.line_edit_tariff.setText(str(tariff[3]))
                self.pay_gaz.line_edit_tariff.setText(str(tariff[4]))

                if float(self.win_pole[2].text()) != 0:
                    self.data_multi.append(self.multiplication(0))
                    self.data_multi.append(self.multiplication(3))
                    self.data_multi.append(self.multiplication(6))

            elif self.pay_power.line_edit_quantity.text():  # если значения нет (берем значение из предыдущего месяца)
                previous_month = month[self.comboBox_month_PAY.currentIndex() - 1]
                if previous_month in tariff[1]:
                    self.pay_power.line_edit_tariff.setText(str(tariff[2]))
                    self.pay_water.line_edit_tariff.setText(str(tariff[3]))
                    self.pay_gaz.line_edit_tariff.setText(str(tariff[4]))

                    if float(self.pay_power.line_edit_tariff.text()) != 0:
                        self.data_multi.append(self.multiplication(0))
                        self.data_multi.append(self.multiplication(3))
                        self.data_multi.append(self.multiplication(6))

            previous_month = month[self.comboBox_month_PAY.currentIndex() - 1]
            if previous_month in tariff[1]:
                self.tariff_water = tariff[3]
                if int(self.comboBox_year_PAY.currentText()) == 2016:
                    if self.comboBox_month_PAY.currentIndex() + 1 == 6:
                        self.tariff_water = self.tariff_water / 10000

        if self.pay_water.line_edit_sum.text():
            self.water_sum = self.quantity * self.tariff_water
            self.pay_apartment.line_edit_minus_water.setText(denomination(int(self.comboBox_year_PAY.currentText()),
                                                                          self.comboBox_month_PAY.currentIndex(),
                                                                          self.water_sum) + " (" + str(self.quantity) +
                                                             ") " + month[self.comboBox_month_PAY.currentIndex() - 1])

        # читаем таблицу с ПЛАТЕЖАМИ
        read_table_payments = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_payments)

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_payments)):
            payment = read_table_payments[i]  # показания сохраненного периода

            # если есть сохраненные значения в таблице для данного периода
            current_month = month[self.comboBox_month_PAY.currentIndex()]
            if current_month in payment[1]:
                self.pay_apartment.line_edit_sum.setText(denomination(int(self.comboBox_year_PAY.currentText()),
                                                                      self.comboBox_month_PAY.currentIndex(),
                                                                      payment[5]))
                self.pay_internet.line_edit_sum.setText(denomination(int(self.comboBox_year_PAY.currentText()),
                                                                     self.comboBox_month_PAY.currentIndex(),
                                                                     payment[6]))
                self.pay_phone.line_edit_sum.setText(denomination(int(self.comboBox_year_PAY.currentText()),
                                                                  self.comboBox_month_PAY.currentIndex(),
                                                                  payment[7]))
                self.apart_summa(self.pay_apartment.line_edit_sum, 9)

                self.status = payment[8]
                self.status = str_list(self.status)
                payment_checked(self.list_payments, self.status)
                self.status = str_list(self.status)

                if self.status == "1 1 1 1 1 1":
                    self.btn_check_all.setChecked(True)
                    self.label_GL_V_1_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
                    self.label_GL_V_2_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))

        self.pay_power.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(0))
        self.pay_water.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(3))
        self.pay_gaz.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(6))

        self.pay_apartment.line_edit_sum.textEdited[str].connect(self.final_summa)
        self.pay_internet.line_edit_sum.textEdited[str].connect(self.final_summa)
        self.pay_phone.line_edit_sum.textEdited[str].connect(self.final_summa)

        self.pay_apartment.line_edit_sum.textEdited[str].connect(lambda: self.apart_summa(
            self.pay_apartment.line_edit_sum, 9))
        self.pay_internet.line_edit_sum.textEdited[str].connect(lambda: self.apart_summa(
            self.pay_internet.line_edit_sum, 10))
        self.pay_phone.line_edit_sum.textEdited[str].connect(lambda: self.apart_summa(
            self.pay_phone.line_edit_sum, 11))

        self.final_summa()

    def check_btn_status(self, checked):
        sender = self.sender()

        index = self.list_payments_name.index(sender.text())
        if checked:
            self.status = str_list(self.status)
            self.status[index] = 1
            self.status = str_list(self.status)
        else:
            self.status = str_list(self.status)
            self.status[index] = 0
            self.status = str_list(self.status)

        if self.status == "1 1 1 1 1 1":
            self.btn_check_all.setChecked(True)
            self.label_GL_V_1_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
            self.label_GL_V_2_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
        else:
            self.btn_check_all.setChecked(False)
            self.label_GL_V_1_PAY.clear()
            self.label_GL_V_2_PAY.clear()

    def check_btn_status_all(self):
        if self.btn_check_all.isChecked():
            for i in self.list_payments:
                i.setChecked(True)
            self.status = "1 1 1 1 1 1"
            self.label_GL_V_1_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
            self.label_GL_V_2_PAY.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
        elif not self.btn_check_all.isChecked():
            read_table_payments = SQLite3_Data_Base.sqlite3_read_data(
                self.data_base, 'Payments_year_' + str(self.comboBox_year_PAY.currentText()))

            # ищем если в таблице значение для выбранного периода (месяц, год)
            for i in range(len(read_table_payments)):
                payment = read_table_payments[i]  # показания сохраненного периода

                # если есть сохраненные значения в таблице для данного периода
                current_month = month[self.comboBox_month_PAY.currentIndex()]
                if current_month in payment[1]:
                    self.status = payment[8]
                    self.status = str_list(self.status)
                    payment_checked(self.list_payments, self.status)
                    self.status = str_list(self.status)
                else:
                    for _ in self.list_payments:
                        _.setChecked(False)
                    self.status = "0 0 0 0 0 0"
            self.label_GL_V_1_PAY.clear()
            self.label_GL_V_2_PAY.clear()

    def multiplication(self, n):
        try:
            self.label_error_PAY.clear()

            if self.win_pole[n] == self.pay_power.line_edit_sum:
                if float(self.win_pole[2].text()) >= 0:
                    multi = float(self.win_pole[2].text()) * int(self.win_pole[1].text())
                    multi = denomination(int(self.comboBox_year_PAY.currentText()),
                                         self.comboBox_month_PAY.currentIndex(), multi)
                    self.win_pole[n].setText(multi)
            elif self.win_pole[n] == self.pay_water.line_edit_sum:
                if float(self.win_pole[5].text()) >= 0:
                    multi = float(self.win_pole[5].text()) * int(self.win_pole[4].text())
                    multi = denomination(int(self.comboBox_year_PAY.currentText()),
                                         self.comboBox_month_PAY.currentIndex(), multi)
                    self.win_pole[n].setText(multi)
            elif self.win_pole[n] == self.pay_gaz.line_edit_sum:
                if float(self.win_pole[8].text()) >= 0:
                    multi = float(self.win_pole[8].text()) * int(self.win_pole[7].text())
                    multi = denomination(int(self.comboBox_year_PAY.currentText()),
                                         self.comboBox_month_PAY.currentIndex(), multi)
                    self.win_pole[n].setText(multi)

            self.final_summa()

            self.data_multi = []  # формируем список сумм за тарифные платежи
            for i in self.win_pole[0:7:3]:
                self.data_multi.append(float(text_convert(i.text())))
        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Должно быть значение!')

    def apart_summa(self, line_edit_sum, win_pole):
        try:
            if line_edit_sum:
                pay = self.win_pole[win_pole].text()
                pay = text_conv_to_num(pay)
                line_edit_sum.setText(num_conv_to_text(pay))
                if line_edit_sum == self.pay_apartment.line_edit_sum:
                    self.balance_sum(pay)
        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Должно быть значение!')

    def balance_sum(self, apart):
        self.water_sum = self.quantity * self.tariff_water

        ost = float(text_conv_to_num(apart)) - self.water_sum
        self.pay_apartment.line_edit_balance_sum.setText(
            denomination(int(self.comboBox_year_PAY.currentText()), self.comboBox_month_PAY.currentIndex(), ost))

    def final_summa(self):
        try:
            self.lineEdit_result.clear()
            final_summa = 0
            if self.pay_power.line_edit_quantity.text():
                if self.pay_power.line_edit_sum.text():
                    for i in self.win_pole[0:7:6]:
                        final_summa += float(text_convert(i.text()))
                if self.pay_apartment.line_edit_sum.text():
                    final_summa += float(text_convert(self.win_pole[9].text()))
                if self.pay_internet.line_edit_sum.text():
                    final_summa += float(text_convert(self.win_pole[10].text()))
                if self.pay_phone.line_edit_sum.text():
                    final_summa += float(text_convert(self.win_pole[11].text()))

                self.lineEdit_result.setText(denomination(int(self.comboBox_year_PAY.currentText()),
                                                          self.comboBox_month_PAY.currentIndex(),
                                                          final_summa) + " руб.")
        except ValueError:
            pass

    def create_list_date(self, name_table, win_pole):  # список показаний за месяц
        data = [self.comboBox_month_PAY.currentIndex() + 1,
                self.comboBox_month_PAY.currentText() + " " + self.comboBox_year_PAY.currentText(), name_table]
        try:
            if win_pole == self.win_pole[9:12]:
                data.extend(self.data_multi)  # добавляем список с суммами за тарифные платежи
                if self.pay_apartment.line_edit_sum.text():
                    for field in win_pole:  # добавляем суммами за остальные платежи
                        data.append(float(text_convert(field.text())))
                    data.append(self.status)
            else:
                for field in win_pole:
                    data.append(float(field.text()))

        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Нет значений для этого периода')

        return data

    def btn_save_PAY(self):
        self.list_data_tariff = self.create_list_date("Tariff", self.win_pole[2:9:3])
        self.list_data_payments = self.create_list_date("Payments", self.win_pole[9:12])
        self.save_payment(self.list_data_tariff, self.list_data_payments)

    def save_payment(self, *args):
        for list_data in args:
            if len(list_data) > 3:
                data = list_data  # создает список значений
                name_table = data[2] + '_year_' + data[1].split()[1]  # Имя таблицы ("1")
                col_name = 'id'  # Имя колонки
                row_record = data[0]  # Имя записи ("1")

                col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, name_table, col_name)

                if row_record in col_id:
                    self.save_yes_or_not(self.data_base, data, self.label_error_PAY)
                else:
                    if data[2] == "Payments":
                        self.next_period()
                    data.remove(data[2])
                    SQLite3_Data_Base.sqlite3_insert_data(self.data_base, name_table, data)
                    self.read_data_pay()

    def next_period(self):
        if self.comboBox_month_PAY.currentIndex() + 2 != 13:
            b = month[self.comboBox_month_PAY.currentIndex() + 1]
            c = self.comboBox_year_PAY.currentText()
        else:
            b = month[self.comboBox_month_PAY.currentIndex() - 11]
            c = str(int(self.comboBox_year_PAY.currentText()) + 1)

        self.label_month_year_PAY.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
        self.comboBox_month_PAY.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_PAY.setCurrentText(c)  # устанавливает текущий год ("Год")

        self.current_month_index = self.period_PAY.label_sel_period()

    def save_yes_or_not(self, data_base, date, label_error):
        self.save_or_PAY = Save_OR()
        self.save_or_PAY.save_yes_or_not(data_base, date, label_error)

    def btn_cancel_PAY(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PAY = CommunalPayment()
    sys.exit(app.exec_())
