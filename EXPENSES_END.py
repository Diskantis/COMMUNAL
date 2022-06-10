# -*- coding: utf-8 -*-

import sys
import win32api
from PyQt5.QtCore import QEvent

from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_COMM import *
from res.UIC_CLASS_COMM import UiWinDialog

from EXPENSES_UIC import UiWinIncomeExpenses


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class IncomeExpenses(QtWidgets.QWidget, UiWinIncomeExpenses):
    def __init__(self):
        super(IncomeExpenses, self).__init__()

        self.setupUi_IAE(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных
        self.record = []

        self.period_IAE = Period(self.comboBox_month_IAE, self.comboBox_year_IAE, self.label_month_year_IAE)
        self.save_or_IAE = Save_OR()

        # ВЫБОР ПЕРИОДА
        selected_period(self.comboBox_month_IAE, self.comboBox_year_IAE)
        self.comboBox_month_IAE.activated.connect(self.combo_box_period_sel)  # месяц
        self.comboBox_year_IAE.activated.connect(self.combo_box_period_sel)  # год

        # ТЕКУЩЕГО ПЕРИОДА
        self.current_month_index = month.index(convert_month(dt_month))  # Текущий месяц (int(0))

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_IAE.setText(convert_month(dt_month) + " " + dt_year)  # заголовок ("Месяц Год")
        self.comboBox_month_IAE.setCurrentIndex(self.current_month_index)  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_IAE.setCurrentText(dt_year)  # устанавливает текущий год ("Год")

        self.btn_Left_IAE.clicked.connect(self.btn_period_left)  # прокрутка в лево
        self.btn_Right_IAE.clicked.connect(self.btn_period_right)  # прокрутка в право
        self.btn_add_iae.clicked.connect(self.add_payment)

        self.win_pole = [self.label_GL_V_1_IAE, self.label_GL_V_2_IAE, self.label_error_IAE]

        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.win_pole.append(self.pay_internet.line_edit_sum)
        # self.v_layout_scrollArea_inc.addWidget(self.pay_internet)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)
        #
        # self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.append(self.pay_apartment.line_edit_sum)
        # self.v_layout_scrollArea_exp.addWidget(self.pay_apartment)

        self.btn_Save_IAE.clicked.connect(self.btn_save_IAE)
        self.btn_Cancel_IAE.clicked.connect(self.btn_cancel_IAE)

        # ЧИТАЕМ показания из базы данных
        self.read_date_income_expenses()

        self.show()

    def moveEvent(self, event):
        if event.type() == QEvent.Move:
            self.win_pos = [int(self.WinIncomeExpenses.geometry().x() + 400),
                            int(self.WinIncomeExpenses.geometry().y() + 200)]
        return super(IncomeExpenses, self).moveEvent(event)

    def combo_box_period_sel(self):
        self.current_month_index = self.period_IAE.label_sel_period()
        if self.comboBox_year_IAE.currentText() == "2006":
            if self.comboBox_month_IAE.currentIndex() <= 5:
                self.comboBox_month_IAE.setCurrentIndex(5)
                self.label_month_year_IAE.setText("Июнь 2006")
                self.current_month_index = 5
        self.read_data_pay()

    def btn_period_left(self):
        self.combo_box_period_sel()
        if self.label_month_year_IAE.text() == "Июнь 2006":
            self.btn_Left_IAE.setEnabled(False)
        else:
            self.current_month_index = self.period_IAE.click_btn_left(self.current_month_index)
            self.read_date_income_expenses()

    def btn_period_right(self):
        self.combo_box_period_sel()
        if self.label_month_year_IAE.text() != "Май 2006":
            self.btn_Left_IAE.setEnabled(True)
            self.current_month_index = self.period_IAE.click_btn_right(self.current_month_index)
            self.read_date_income_expenses()

    def add_payment(self):
        self.new_record = IAENewRecord()
        self.new_record.win_sel_type_rec(self.win_pos)

    # # добавление нового платежа
    # def win_add_name_pay(self):
    #     self.win_name_pay = UiWinDialog()
    #     self.win_name_pay.setupUi_Dialog()
    #
    #     if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
    #         win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский  00000419
    #
    #     # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
    #     self.win_name_pay.add_pay_btn_OK.clicked.connect(self.win_add_summa_pay)  # OK
    #     self.win_name_pay.add_pay_btn_OK.setAutoDefault(True)
    #     self.win_name_pay.lineEdit.returnPressed.connect(self.win_name_pay.add_pay_btn_OK.click)
    #
    #     self.win_name_pay.add_pay_btn_Cancel.clicked.connect(lambda: self.win_add_cancel(self.win_name_pay))  # CANCEL
    #
    # def win_add_summa_pay(self):
    #     self.name_pay = self.win_name_pay.lineEdit.text()
    #     self.win_name_pay.lineEdit.clear()
    #     self.win_name_pay.close()
    #
    #     self.win_summa_pay = UiWinDialog()
    #     self.win_summa_pay.setupUi_Dialog()
    #     self.win_summa_pay.label.setText("Сумма платежа")
    #
    #     if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
    #         win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский  00000419
    #
    #     self.win_summa_pay.add_pay_btn_OK.clicked.connect(self.add_payment)  # кнопка OK окна СУММА
    #     self.win_summa_pay.add_pay_btn_OK.setAutoDefault(True)
    #     self.win_summa_pay.lineEdit.returnPressed.connect(self.win_summa_pay.add_pay_btn_OK.click)
    #
    #     self.win_summa_pay.add_pay_btn_Cancel.clicked.connect(lambda: self.win_add_cancel(self.win_summa_pay))
    #
    # def add_payment(self):
    #     self.summa_pay = self.win_summa_pay.lineEdit.text()
    #     self.summa_pay_text = text_convert(self.summa_pay)
    #
    #     self.payment = Widget_Payment(self.name_pay, "(209, 209, 217)")
    #     self.payment.line_edit_sum.setText(self.summa_pay_text + " руб")
    #     self.win_pole.append(self.payment.line_edit_sum)
    #     self.v_layout_scrollArea.addWidget(self.payment)
    #
    #     # # возможно удаление после того как был создан доп. плат.
    #     # self.new_p.btn_del_Plat.clicked.connect(self.new_p.deleteLater)
    #     # self.new_p.btn_del_Plat.clicked.connect(self.btn_del_plateg)
    #
    #     self.win_summa_pay.lineEdit.clear()
    #     self.win_summa_pay.close()
    #
    # @staticmethod
    # def win_add_cancel(app_win):
    #     app_win.lineEdit.clear()
    #     app_win.close()

    def read_date_income_expenses(self):
        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский 00000419

        file_db = open('COMMPAY_DAT.db', 'a')  # открывает файл базы данных
        file_db.close()  # закрывает файл базы данных

        table_count = 'Counters_year_' + str(self.comboBox_year_IAE.currentText())  # имя таблицы
        table_tariff = 'Tariff_year_' + str(self.comboBox_year_IAE.currentText())  # имя таблицы
        table_payments = 'Payments_year_' + str(self.comboBox_year_IAE.currentText())  # имя таблицы

        # col_name = 'id'  # Имя колонки

        # заголовок атрибутов таблицы Tariff
        heading_tariff = 'id integer primary key , month_year text, ' \
                         'Tariff_PW integer, Tariff_WA integer, Tariff_GZ integer'

        # создает таблицу в базе данных, это нужно если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_tariff, heading_tariff)
        
        # заголовок атрибутов таблицы Payments
        heading_payments = 'id integer primary key , month_year text, name_payment text, summa integer'

        # создает таблицу в базе данных, это нужно если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_payments, heading_payments)

        for i in self.win_pole:  # очищает поля окна ПОКАЗАНИЯ
            i.clear()

        read_table = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_count)

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table)):
            pred_pokaz = read_table[i]  # показания сохраненного периода
            # print(pred_pokaz)

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_IAE.text() == pred_pokaz[1]:
                self.pay_power.line_edit_quantity.setText(str(pred_pokaz[3] - pred_pokaz[2]))
                self.pay_water.line_edit_quantity.setText(str((pred_pokaz[5] - pred_pokaz[4]) +
                                                              (pred_pokaz[7] - pred_pokaz[6]) +
                                                              (pred_pokaz[9] - pred_pokaz[8]) +
                                                              (pred_pokaz[11] - pred_pokaz[10])))
                self.pay_gaz.line_edit_quantity.setText(str(pred_pokaz[13] - pred_pokaz[12]))

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

    # создает список значений полей для записи в таблицу
    def create_list_date(self):  # список показаний за месяц
        data = [self.comboBox_month_IAE.currentIndex() + 1,
                self.comboBox_month_IAE.currentText() + " " + self.comboBox_year_IAE.currentText()]
        try:
            for field in self.win_pole[0:12]:
                data.append(int(field.text()))
        except ValueError:
            self.label_error_IAE.show()
            self.label_error_IAE.setText('Нет значений для этого периода')
        return data

    def btn_save_IAE(self):
        pass

    def btn_cancel_IAE(self):
        self.close()

    def save_yes_or_not(self):
        pass

    def save_yn_btn_ok(self):
        pass

    def save_yn_btn_cancel(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_IAE = IncomeExpenses()
    sys.exit(app.exec_())
