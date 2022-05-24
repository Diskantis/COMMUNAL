# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_COMM import *
from res.UIC_CLASS_COMM import UiWinAdd

from COMMPAY_UIC import UiWinPayment


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class CommunalPayment(QtWidgets.QWidget, UiWinPayment):
    def __init__(self):
        super(CommunalPayment, self).__init__()

        self.setupUi_PAY(self)
        self.saveUi_PAY = UiWinAdd()

        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных
        self.data_mult = []

        self.period_PAY = Period(self.comboBox_month_PAY, self.comboBox_year_PAY, self.label_month_year_PAY)
        self.save_or_PAY = Save_OR()

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

        self.win_pole = [self.pay_power.line_edit_sum, self.pay_power.line_edit_tariff,
                         self.pay_water.line_edit_sum, self.pay_water.line_edit_tariff,
                         self.pay_gaz.line_edit_sum, self.pay_gaz.line_edit_tariff,
                         self.pay_apartment.line_edit_sum,
                         self.pay_internet.line_edit_sum,
                         self.pay_phone.line_edit_sum,
                         self.label_GL_V_1_PAY, self.label_GL_V_2_PAY, self.label_error_PAY]

        self.btn_Save_PAY.clicked.connect(self.btn_save_PAY)
        self.btn_Cancel_PAY.clicked.connect(self.btn_cancel_PAY)

        # ЧИТАЕМ показания из базы данных
        self.read_data_pay()

        self.show()

    def start_period(self):
        if self.label_month_year_PAY.text() == 'Декабрь 2006' and self.comboBox_month_PAY.count() == 12 \
                or int(self.comboBox_year_PAY.currentText()) == 2006 and self.comboBox_month_PAY.currentIndex() <= 11 \
                and self.comboBox_month_PAY.count() == 12:
            self.comboBox_month_PAY.clear()
            self.comboBox_month_PAY.addItems(month[5:12])
        elif self.label_month_year_PAY.text() == 'Декабрь 2006' and self.comboBox_month_PAY.count() == 7 \
                or int(self.comboBox_year_PAY.currentText()) >= 2007 and self.comboBox_month_PAY.currentIndex() >= 0 \
                and self.comboBox_month_PAY.count() == 7:
            self.comboBox_month_PAY.clear()
            self.comboBox_month_PAY.addItems(month)

    def label_period(self):
        self.start_period()
        self.current_month_index = self.period_PAY.label_sel_period()
        self.read_data_pay()

    def btn_period_left(self):
        self.start_period()
        if self.label_month_year_PAY.text() == "Июнь 2006":
            self.btn_Left_PAY.setEnabled(False)
        else:
            self.current_month_index = self.period_PAY.click_btn_left(self.current_month_index)
            self.read_data_pay()

    def btn_period_right(self):
        self.start_period()
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

        # col_name = 'id'  # Имя колонки

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

        for i in self.win_pole:  # очищает поля окна ПОКАЗАНИЯ
            i.clear()

        # читаем таблицу с ПОКАЗАНИЯМИ СЧЕТЧИКОВ
        read_table_counters = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_counters)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_counters)):
            counter = read_table_counters[i]  # показания сохраненного периода

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_PAY.text() == counter[1]:
                self.pay_power.line_edit_quantity.setText(str(counter[3] - counter[2]))
                self.pay_water.line_edit_quantity.setText(str((counter[5] - counter[4]) +
                                                              (counter[7] - counter[6]) +
                                                              (counter[9] - counter[8]) +
                                                              (counter[11] - counter[10])))
                self.pay_gaz.line_edit_quantity.setText(str(counter[13] - counter[12]))

        # читаем таблицу с ТАРИФАМИ
        read_table_tariff = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_tariff)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_tariff)):
            tariff = read_table_tariff[i]  # показания сохраненного периода

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_PAY.text() == tariff[1]:
                # присваиваем полям значения выбранного периода из сохраненной таблицы
                for a, b in zip(self.win_pole[1:6:2], range(2, 5)):
                    a.setText(str(tariff[b]))

                if float(self.win_pole[1].text()) != 0:
                    self.data_mult.append(self.multiplication(0))
                    self.data_mult.append(self.multiplication(2))
                    self.data_mult.append(self.multiplication(4))
                break
            else:  # если значения не совпадают (берем значение "ПОСЛЕДНЕЕ" из предыдущего месяца)
                pred_month = month[self.comboBox_month_PAY.currentIndex() - 1]
                if pred_month in tariff[1]:
                    # присваиваем полям "ПРЕДЫДУЩИЕ", значения из сохраненной таблицы
                    for c, d in zip(self.win_pole[1:6:2], range(2, 5)):
                        c.setText(str(tariff[d]))

                    if float(self.win_pole[1].text()) != 0:
                        self.data_mult.append(self.multiplication(0))
                        self.data_mult.append(self.multiplication(2))
                        self.data_mult.append(self.multiplication(4))

                # self.pay_power.line_edit_tariff.setText(str(tariff[2]))
                # self.pay_water.line_edit_tariff.setText(str(tariff[3]))
                # self.pay_gaz.line_edit_tariff.setText(str(tariff[4]))

                # if float(self.win_pole[1].text()) != 0:
                #     self.data_mult.append(self.multiplication(0))
                #     self.data_mult.append(self.multiplication(2))
                #     self.data_mult.append(self.multiplication(4))

        # читаем таблицу с ПЛАТЕЖАМИ
        read_table_payments = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_payments)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table_payments)):
            payment = read_table_payments[i]  # показания сохраненного периода

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_PAY.text() == payment[1]:

                # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
                if self.label_month_year_PAY.text() == payment[1]:
                    self.pay_apartment.line_edit_sum.setText(str(payment[5]))
                    self.pay_internet.line_edit_sum.setText(str(payment[6]))
                    self.pay_phone.line_edit_sum.setText(str(payment[7]))

        self.pay_power.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(0))
        self.pay_water.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(2))
        self.pay_gaz.line_edit_tariff.textEdited[str].connect(lambda: self.multiplication(4))

    # присваиваем полям значения выбранного периода из сохраненной таблицы
    #     for a, b in zip(self.win_pole[:12], range(2, 14)):  # range = heading поля с 2 по 13
    #         a.setText(str(pred_pokaz[b]))
    #     break
    # else:  # если значения не совпадают (берем значение "ПОСЛЕДНЕЕ" из предыдущего месяца)
    #     pred_month = month[self.comboBox_month_COU.currentIndex() - 1]
    #     if pred_month in pred_pokaz[1]:
    #         # присваиваем полям "ПРЕДЫДУЩИЕ", значения из сохраненной таблицы
    #         for c, d in zip(self.win_pole[:11:2], range(3, 14, 2)):
    #             c.setText(str(pred_pokaz[d]))
    #         # а полям "ПОСЛЕДНЕЕ" и "месячный расход" присваиваем значения "0"
    #         for j in self.win_pole[1: 12: 2] + self.win_pole[12: 17]:
    #             j.setText("0")

    def multiplication(self, n):
        try:
            self.label_error_PAY.clear()
            self.win_pole[n].setText("0")
            if self.win_pole[n] == self.pay_power.line_edit_sum:
                if float(self.win_pole[1].text()) != 0:
                    multi = float(self.win_pole[1].text()) * int(self.pay_power.line_edit_quantity.text())
                    multi = round(multi, 2)
                    self.win_pole[n].setText(str(multi))
            elif self.win_pole[n] == self.pay_water.line_edit_sum:
                if float(self.win_pole[3].text()) != 0:
                    multi = float(self.win_pole[3].text()) * int(self.pay_water.line_edit_quantity.text())
                    multi = round(multi, 2)
                    self.win_pole[n].setText(str(multi))
            elif self.win_pole[n] == self.pay_gaz.line_edit_sum:
                if float(self.win_pole[5].text()) != 0:
                    multi = float(self.win_pole[5].text()) * int(self.pay_gaz.line_edit_quantity.text())
                    multi = round(multi, 2)
                    self.win_pole[n].setText(str(multi))

            self.data_mult = []
            for i in self.win_pole[0:6:2]:
                self.data_mult.append(float(i.text()))
        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Должно быть значение!')

    def btn_save_PAY(self):
        list_data_tariff = self.list_date(self.win_pole[1:6:2])
        list_data_payments = self.list_date(self.win_pole[6:9])
        self.save_payment("Tariff", list_data_tariff)
        self.save_payment("Payments", list_data_payments)
        self.read_data_pay()

    def list_date(self, win_pole):  # список показаний за месяц
        data = [self.comboBox_month_PAY.currentIndex() + 1,
                self.comboBox_month_PAY.currentText() + " " + self.comboBox_year_PAY.currentText()]
        try:
            if win_pole == self.win_pole[6:9]:
                data.extend(self.data_mult)
                for field in win_pole:
                    sum_pay = float(field.text())
                    sum_pay = float('{:.2f}'.format(sum_pay))
                    data.append(sum_pay)
            else:
                for field in win_pole:
                    data.append(float(field.text()))

        except ValueError:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Нет значений для этого периода')
        return data

    def save_payment(self, name_table, list_data):
        data = list_data  # создает список значений
        table = name_table + '_year_' + data[1].split()[1]  # Имя таблицы ("1")
        col_name = 'id'  # Имя колонки
        row_record = data[0]  # Имя записи ("1")

        col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]

        if row_record in col_id:
            self.label_error_PAY.show()
            self.label_error_PAY.setText('Такая запись уже существует!')
            self.save_yes_or_not()
        else:
            SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, data)

            if self.comboBox_month_PAY.currentIndex() + 2 != 13:
                b = month[self.comboBox_month_PAY.currentIndex() + 1]
                c = self.comboBox_year_PAY.currentText()
            else:
                b = month[self.comboBox_month_PAY.currentIndex() - 11]
                c = str(int(self.comboBox_year_PAY.currentText()) + 1)

            self.label_month_year_PAY.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
            self.comboBox_month_PAY.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
            self.comboBox_year_PAY.setCurrentText(c)  # устанавливает текущий год ("Год")

    def btn_cancel_PAY(self):
        self.close()

    def save_yes_or_not(self):
        pass
        # self.save_yn.name_platega()
        # self.save_yn.setWindowTitle("Сохранение")
        #
        # self.save_yn.lineEdit.close()
        # self.save_yn.label_pust.setGeometry(QtCore.QRect(10, 0, 270, 70))
        # self.save_yn.label_pust.setText("Вы действительно хотите \n перезаписать показания?")
        #
        # self.save_yn.btn_OK.clicked.connect(self.save_yn_btn_ok)
        # self.save_yn.btn_OK.setAutoDefault(True)
        # self.save_yn.btn_Cancel.clicked.connect(self.save_yn_btn_cancel)

    def save_yn_btn_ok(self):
        pass
        # table = 'Pokazanya_year_' + self.data[1].split()[1]  # имя таблицы (период)
        # col_name = 'id'  # имя колонки
        # row_record = self.data[0]  # имя записи

        # SQLite3_Data_Base.sqlite3_delete_record(self.data_base, table, col_name, str(row_record))  # удаляем запись
        # SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, self.data)  # вставляем изменённую запись

        # self.read_pokaz_schet()
        # self.label_error_PAY.hide()
        # self.save_yn.close()

    def save_yn_btn_cancel(self):
        pass
        # self.label_error_PAY.hide()
        # self.save_yn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PAY = CommunalPayment()
    sys.exit(app.exec_())
