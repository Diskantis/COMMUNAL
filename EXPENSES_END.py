# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_COMM import *
from res.UIC_CLASS_COMM import label_titul_f

from EXPENSES_UIC import UiWinIncomeExpenses


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class IncomeExpenses(QtWidgets.QWidget, UiWinIncomeExpenses):
    def __init__(self):
        super(IncomeExpenses, self).__init__()

        self.setupUi_IAE(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных
        self.records_income = []
        self.records_expense = []
        self.status = ""

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
        self.btn_add_iae.clicked.connect(self.win_sel_type_rec)

        self.win_pole = [self.label_GL_V_1_IAE, self.label_GL_V_2_IAE, self.label_error_IAE]

        self.btn_Save_IAE.clicked.connect(self.btn_save_IAE)
        self.btn_Cancel_IAE.clicked.connect(self.btn_cancel_IAE)

        # ЧИТАЕМ показания из базы данных
        # self.read_date_income_expenses()

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
        # self.read_date_income_expenses()

    def btn_period_left(self):
        self.combo_box_period_sel()
        if self.label_month_year_IAE.text() == "Июнь 2006":
            self.btn_Left_IAE.setEnabled(False)
        else:
            self.current_month_index = self.period_IAE.click_btn_left(self.current_month_index)
            # self.read_date_income_expenses()

    def btn_period_right(self):
        self.combo_box_period_sel()
        if self.label_month_year_IAE.text() != "Май 2006":
            self.btn_Left_IAE.setEnabled(True)
            self.current_month_index = self.period_IAE.click_btn_right(self.current_month_index)
            # self.read_date_income_expenses()

    def win_sel_type_rec(self):
        self.records = [1]
        self.new_rec = IAENewRecord(self.win_pos)
        self.records = self.new_rec.win_sel_type_rec()

        self.new_rec.win_new_rec.add_pay_btn_OK.clicked.connect(self.win_rec_name)  # OK
        self.new_rec.win_new_rec.add_pay_btn_OK.setAutoDefault(True)

        self.new_rec.win_new_rec.add_pay_btn_Cancel.clicked.connect(
            lambda: self.win_add_cancel(self.new_rec.win_new_rec))  # CANCEL

    def win_rec_name(self):
        self.new_rec.win_new_rec.close()
        self.new_rec = IAENewRecord(self.win_pos)
        self.new_rec.win_rec_name()

        self.new_rec.win_rec_name.add_pay_btn_OK.clicked.connect(self.win_rec_summa)  # OK
        self.new_rec.win_rec_name.add_pay_btn_OK.setAutoDefault(True)
        self.new_rec.win_rec_name.lineEdit.returnPressed.connect(self.new_rec.win_rec_name.add_pay_btn_OK.click)

        self.new_rec.win_rec_name.add_pay_btn_Cancel.clicked.connect(
            lambda: self.win_add_cancel(self.new_rec.win_rec_name))  # CANCEL

    def win_rec_summa(self):
        self.records.append(self.new_rec.win_rec_name.lineEdit.text())
        self.new_rec.win_rec_name.lineEdit.clear()
        self.new_rec.win_rec_name.close()

        self.new_rec = IAENewRecord(self.win_pos)
        self.new_rec.win_rec_summa()

        self.new_rec.win_rec_summa.add_pay_btn_OK.clicked.connect(self.add_record)  # OK
        self.new_rec.win_rec_summa.add_pay_btn_OK.setAutoDefault(True)
        self.new_rec.win_rec_summa.lineEdit.returnPressed.connect(self.new_rec.win_rec_summa.add_pay_btn_OK.click)

        self.new_rec.win_rec_summa.add_pay_btn_Cancel.clicked.connect(
            lambda: self.win_add_cancel(self.new_rec.win_rec_summa))  # CANCEL

    def add_record(self):
        self.records.append(float(self.new_rec.win_rec_summa.lineEdit.text()))
        self.new_rec.win_rec_summa.lineEdit.clear()
        self.new_rec.win_rec_summa.close()

        self.new_record = Widget_Payment(self.records[1], "(209, 209, 217)")
        self.new_record.btn_check.setFixedSize(QtCore.QSize(247, 28))
        self.new_record.line_edit_sum.setFixedSize(QtCore.QSize(100, 28))
        self.new_record.line_edit_sum.setText(str(self.records[2]))

        if self.records[0] == 0:
            rec_name = self.new_record.btn_check.text()
            self.new_record.btn_check.deleteLater()
            self.label = label_titul_f(rec_name, self.new_record, 12)
            self.label.setFixedSize(QtCore.QSize(247, 28))
            self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.new_record.h_Layout_widget_Team.insertWidget(0, self.label)

            self.v_layout_scrollArea_inc.addWidget(self.new_record)

            record_income = [self.records[1], self.records[2]]
            self.records_income.append(record_income)
        elif self.records[0] == 1:
            self.v_layout_scrollArea_exp.addWidget(self.new_record)

            print(self.new_record.btn_check.isChecked())
            record_expense = [self.records[1], self.records[2]]
            self.records_expense.append(record_expense)

        self.records.clear()

    def read_date_income_expenses(self):
        file_db = open('COMMPAY_DAT.db', 'a')  # открывает файл базы данных
        file_db.close()  # закрывает файл базы данных

        table_incomes = 'Income_year_' + str(self.comboBox_year_IAE.currentText())  # имя таблицы
        table_expenses = 'Expenses_year_' + str(self.comboBox_year_IAE.currentText())  # имя таблицы

        # заголовок атрибутов таблицы Income
        heading_incomes = 'id integer primary key , month_year text, Income_name text, Income_summa integer'

        # заголовок атрибутов таблицы Expenses
        heading_expenses = 'id integer primary key , month_year text, Expense_name text, Expense_summa integer, ' \
                           'Status text'

        # создает таблицу в базе данных, это нужно если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_incomes, heading_incomes)
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table_expenses, heading_expenses)

        # очищает поля окна ПОКАЗАНИЯ
        clear_layout(self.v_layout_scrollArea_inc)
        clear_layout(self.v_layout_scrollArea_exp)

        read_table = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_incomes)

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table)):
            rec_incomes = read_table[i]  # показания сохраненного периода
            # print(rec_incomes)

            # # если лейбл "Месяц Год" совпадает со значением в таблице "Месяц Год"
            # if self.label_month_year_IAE.text() == rec_incomes[1]:
            #     self.new_record = Widget_Payment(self.records[1], "(209, 209, 217)")
            #     rec_name = self.new_record.btn_check.text()
            #     self.new_record.btn_check.deleteLater()
            #     self.label = label_titul_f(rec_name, self.new_record, 12)
            #     self.label.setFixedSize(QtCore.QSize(247, 28))
            #     self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            #     self.new_record.h_Layout_widget_Team.insertWidget(0, self.label)
            #
            #     self.new_record.line_edit_sum.setFixedSize(QtCore.QSize(100, 28))
            #     self.new_record.line_edit_sum.setText(str(self.records[2]))
            #
            #     self.v_layout_scrollArea_inc.addWidget(self.new_record)

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

    def save_yes_or_not(self):
        pass

    def save_yn_btn_ok(self):
        pass

    @staticmethod
    def win_add_cancel(app_win):
        app_win.close()

    def save_yn_btn_cancel(self):
        pass

    def btn_cancel_IAE(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_IAE = IncomeExpenses()
    sys.exit(app.exec_())
