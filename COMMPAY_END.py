# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# from res.DLL_CLASS_COMM import *
from res.DLL_CLASS_COMM import dt_month, dt_year, month, convert_month, selected_period, \
                               Period, Save_OR, SQLite3_Data_Base
from COMMPAY_UIC import UiWinPayment


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class CommunalPayment(QtWidgets.QWidget, UiWinPayment):
    def __init__(self):
        super(CommunalPayment, self).__init__()

        self.setupUi_PAY(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных

        self.data_mult = []

        self.period_PAY = Period(self.comboBox_month_PAY, self.comboBox_year_PAY, self.label_month_year_PAY)

        # ВЫБОР ПЕРИОДА
        selected_period(self.comboBox_month_PAY, self.comboBox_year_PAY)
        self.comboBox_month_PAY.activated.connect(self.label_period)  # месяц
        self.comboBox_year_PAY.activated.connect(self.label_period)  # год

        # ТЕКУЩЕГО ПЕРИОДА
        self.current_month_index = month.index(convert_month(dt_month))  # Текущий месяц (int(0))

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_PAY.setText(convert_month(dt_month) + " " + dt_year)  # заголовок ("Месяц Год")
        self.comboBox_month_PAY.setCurrentIndex(self.current_month_index)  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_PAY.setCurrentText(dt_year)  # устанавливает текущий год ("Год")

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
                         self.pay_apartment.line_edit_minus_water, self.pay_apartment.line_edit_ostat_sum,
                         self.lineEdit_result,
                         self.label_GL_V_1_PAY, self.label_GL_V_2_PAY, self.label_error_PAY]

        self.btn_Save_PAY.clicked.connect(self.btn_save_PAY)
        self.btn_Cancel_PAY.clicked.connect(self.btn_cancel_PAY)

        # ЧИТАЕМ показания из базы данных
        self.read_data_pay()

        self.show()

    # def start_period(self):
    #     if self.label_month_year_PAY.text() == 'Декабрь 2006' and self.comboBox_month_PAY.count() == 12 \
    #             or int(self.comboBox_year_PAY.currentText()) == 2006 and self.comboBox_month_PAY.currentIndex() <= 11 \
    #             and self.comboBox_month_PAY.count() == 12:
    #         self.comboBox_month_PAY.clear()
    #         self.comboBox_month_PAY.addItems(month[5:12])
    #     elif self.label_month_year_PAY.text() == 'Декабрь 2006' and self.comboBox_month_PAY.count() == 7 \
    #             or int(self.comboBox_year_PAY.currentText()) >= 2007 and self.comboBox_month_PAY.currentIndex() >= 0 \
    #             and self.comboBox_month_PAY.count() == 7:
    #         self.comboBox_month_PAY.clear()
    #         self.comboBox_month_PAY.addItems(month)

    def label_period(self):
        # self.start_period()
        self.current_month_index = self.period_PAY.label_sel_period()
        self.read_data_pay()

    def btn_period_left(self):
        # self.start_period()
        if self.label_month_year_PAY.text() == "Июнь 2006":
            self.btn_Left_PAY.setEnabled(False)
        else:
            self.current_month_index = self.period_PAY.click_btn_left(self.current_month_index)
            self.read_data_pay()

    def btn_period_right(self):
        # self.start_period()
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
                           'Summa_AP integer, Summa_IN integer, Summa_PH integer'

        # создает таблицу в базе данных, если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_tariff, heading_tariff)
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_payments, heading_payments)

        for i in self.win_pole:  # очищает поля окна
            i.clear()

        # читаем таблицу с ПОКАЗАНИЯМИ СЧЕТЧИКОВ
        read_table_counters = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_counters)[0]

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

        # читаем таблицу с ТАРИФАМИ
        read_table_tariff = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_tariff)[0]

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
                    self.data_mult.append(self.multiplication(0))
                    self.data_mult.append(self.multiplication(3))
                    self.data_mult.append(self.multiplication(6))
                break
            else:  # если значения нет (берем значение из предыдущего месяца)
                if self.pay_power.line_edit_quantity.text():
                    previous_month = month[self.comboBox_month_PAY.currentIndex() - 1]
                    if previous_month in tariff[1]:
                        self.pay_power.line_edit_tariff.setText(str(tariff[2]))
                        self.pay_water.line_edit_tariff.setText(str(tariff[3]))
                        self.pay_gaz.line_edit_tariff.setText(str(tariff[4]))

                        if float(self.pay_power.line_edit_tariff.text()) != 0:
                            self.data_mult.append(self.multiplication(0))
                            self.data_mult.append(self.multiplication(3))
                            self.data_mult.append(self.multiplication(6))

            previous_month = month[self.comboBox_month_PAY.currentIndex() - 1]
            if previous_month in tariff[1]:
                self.tariff_water = tariff[3]

        # читаем таблицу с ПЛАТЕЖАМИ
        read_table_payments = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_payments)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_payments)):
            payment = read_table_payments[i]  # показания сохраненного периода

            # если есть сохраненные значения в таблице для данного периода
            current_month = month[self.comboBox_month_PAY.currentIndex()]
            if current_month in payment[1]:
                self.pay_apartment.line_edit_sum.setText(str('{:.2f}'.format(payment[5])))
                self.apart_summa()
                self.pay_internet.line_edit_sum.setText(str('{:.2f}'.format(payment[6])))
                self.pay_phone.line_edit_sum.setText(str('{:.2f}'.format(payment[7])))

        self.pay_power.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(0))
        self.pay_water.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(3))
        self.pay_gaz.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(6))

        self.pay_apartment.line_edit_sum.textEdited[str].connect(self.final_summa)
        self.pay_apartment.line_edit_sum.textEdited[str].connect(self.apart_summa)
        self.pay_internet.line_edit_sum.textEdited[str].connect(self.final_summa)
        self.pay_phone.line_edit_sum.textEdited[str].connect(self.final_summa)

        self.final_summa()

    def multiplication(self, n):
        try:
            self.label_error_PAY.clear()

            if self.win_pole[n] == self.pay_power.line_edit_sum:
                if float(self.win_pole[2].text()) != 0:
                    multi = float(self.win_pole[2].text()) * int(self.win_pole[1].text())
                    self.win_pole[n].setText(str('{:.2f}'.format(multi)))
            elif self.win_pole[n] == self.pay_water.line_edit_sum:
                if float(self.win_pole[5].text()) != 0:
                    multi = float(self.win_pole[5].text()) * int(self.win_pole[4].text())
                    self.win_pole[n].setText(str('{:.2f}'.format(multi)))
            elif self.win_pole[n] == self.pay_gaz.line_edit_sum:
                if float(self.win_pole[8].text()) != 0:
                    multi = float(self.win_pole[8].text()) * int(self.win_pole[7].text())
                    self.win_pole[n].setText(str('{:.2f}'.format(multi)))

            self.data_mult = []  # формируем список сумм за тарифные платежи
            for i in self.win_pole[0:7:3]:
                self.data_mult.append(float(i.text()))

        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Должно быть значение!')

    def apart_summa(self):
        if self.pay_apartment.line_edit_sum:
            multi = self.quantity * self.tariff_water
            apart = float(self.win_pole[9].text()) - multi
            self.pay_apartment.line_edit_ostat_sum.setText(str('{:.2f}'.format(apart)))
            self.pay_apartment.line_edit_minus_water.setText(
                str('{:.2f}'.format(multi) + " (" + str(self.quantity) + ") " +
                    month[self.comboBox_month_PAY.currentIndex() - 1]))

    def final_summa(self):
        try:
            # self.label_error_PAY.clear()
            self.lineEdit_result.clear()
            final_summa = 0
            if self.pay_power.line_edit_quantity.text():
                if self.pay_power.line_edit_sum.text():
                    for i in self.win_pole[0:7:6]:
                        final_summa += float(i.text())
                if self.pay_apartment.line_edit_sum.text():
                    for i in self.win_pole[9:12]:
                        final_summa += float(i.text())
                self.lineEdit_result.setText(str('{:.2f}'.format(final_summa)))

        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Должно быть значение')

    def list_date(self, name_table, win_pole):  # список показаний за месяц
        data = [self.comboBox_month_PAY.currentIndex() + 1,
                self.comboBox_month_PAY.currentText() + " " + self.comboBox_year_PAY.currentText(), name_table]
        try:
            if win_pole == self.win_pole[9:12]:
                if self.pay_apartment.line_edit_sum.text():
                    data.extend(self.data_mult)  # добавляем список с суммами за тарифные платежи
                    for field in win_pole:  # добавляем суммами за остальные платежи
                        data.append(float(field.text()))
            else:
                for field in win_pole:
                    data.append(float(field.text()))
        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Нет значений для этого периода')
        return data

    def btn_save_PAY(self):
        list_data_tariff = self.list_date("Tariff", self.win_pole[2:9:3])
        list_data_payments = self.list_date("Payments", self.win_pole[9:12])
        # print(list_data_tariff)
        # print(list_data_payments)
        self.save_payment(list_data_tariff, list_data_payments)
        self.read_data_pay()

    def save_payment(self, *args):
        for list_data in args:
            if len(list_data) > 3:
                data = list_data  # создает список значений
                name_table = data[2] + '_year_' + data[1].split()[1]  # Имя таблицы ("1")
                col_name = 'id'  # Имя колонки
                row_record = data[0]  # Имя записи ("1")
                data.remove(data[2])  # Удаляем имя таблицы из списка "Tariff"

                col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, name_table, col_name)[0]

                if row_record in col_id:
                    self.label_error_PAY.show()
                    self.label_error_PAY.setText("Такая запись уже существует!")
                    self.save_yes_or_not(name_table, self.data_base, data, self.label_error_PAY)
                else:
                    SQLite3_Data_Base.sqlite3_insert_data(self.data_base, name_table, data)
                    self.next_period()

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

    def save_yes_or_not(self, name_table, data_base, date, label_error):
        self.save_or_PAY = Save_OR()
        self.save_or_PAY.save_yes_or_not(name_table, data_base, date, label_error)

    def btn_cancel_PAY(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PAY = CommunalPayment()
    sys.exit(app.exec_())
