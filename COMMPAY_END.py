# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_COMM import *
from res.UIC_CLASS_COMM import UiWinAdd  # NewPlateg

from COMMPAY_UIC import UiWinPayment


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class CommunalPayment(QtWidgets.QWidget, UiWinPayment):
    def __init__(self):
        super(CommunalPayment, self).__init__()

        self.save_yn = UiWinAdd()

        self.setupUi_PAY(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных

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

        self.win_pole = [self.label_GL_V_1_PAY, self.label_GL_V_2_PAY, self.label_error_PAY]

        self.pay_power = Widget_Payment("Электричество", "(0, 160, 0)")
        self.pay_power.commpay()
        self.win_pole.append(self.pay_power.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_power.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_power.line_edit_quantity)
        # self.win_pole.insert(-3, self.pay_power.line_edit_tariff)
        self.v_layout_scrollArea.addWidget(self.pay_power)

        self.pay_water = Widget_Payment("Вода", "(0, 170, 255)")
        self.pay_water.commpay()
        self.win_pole.append(self.pay_water.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_water.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_water.line_edit_quantity)
        # self.win_pole.insert(-3, self.pay_water.line_edit_tariff)
        self.v_layout_scrollArea.addWidget(self.pay_water)

        self.pay_gaz = Widget_Payment("Газ", "(150, 0, 150)")
        self.pay_gaz.commpay()
        self.win_pole.append(self.pay_gaz.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_gaz.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_gaz.line_edit_quantity)
        # self.win_pole.insert(-3, self.pay_gaz.line_edit_tariff)
        self.v_layout_scrollArea.addWidget(self.pay_gaz)

        self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        # self.win_pole.insert(-3, self.pay_apartment.line_edit_sum)
        # self.win_pole.insert(-3, self.pay_apartment.line_edit_quantity)
        # self.win_pole.insert(-3, self.pay_apartment.line_edit_tariff)
        self.v_layout_scrollArea.addWidget(self.pay_apartment)

        # # РАЗДЕЛИТЕЛЬ между основными и дополнительными платежами
        self.Line_razdel = QtWidgets.QFrame()
        self.Line_razdel.setFixedSize(QtCore.QSize(740, 5))
        self.Line_razdel.setAutoFillBackground(False)
        self.Line_razdel.setContentsMargins(5, 0, 0, 0)
        self.Line_razdel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line_razdel.setLineWidth(1)
        self.Line_razdel.setMidLineWidth(1)
        self.Line_razdel.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line_razdel.setObjectName("LINE_RAZDEL")
        self.v_layout_scrollArea.addWidget(self.Line_razdel)

        self.btn_Save_PAY.clicked.connect(self.btn_save_PAY)
        self.btn_Cancel_PAY.clicked.connect(self.btn_cancel_PAY)

        # self.pay_apartment = Widget_Payment("Интернет", "(209, 209, 217)")
        # self.v_layout_scrollArea.addWidget(self.pay_apartment)

        # self.pay_apartment = Widget_Payment("Телефон", "(209, 209, 217)")
        # self.v_layout_scrollArea.addWidget(self.pay_apartment)

        print(self.win_pole)

        # ЧИТАЕМ показания из базы данных
        self.read_pokaz()

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
        self.read_pokaz()

    def btn_period_left(self):
        self.start_period()
        if self.label_month_year_PAY.text() == "Июнь 2006":
            self.btn_Left_PAY.setEnabled(False)
        else:
            self.current_month_index = self.period_PAY.click_btn_left(self.current_month_index)
            self.read_pokaz()

    def btn_period_right(self):
        self.start_period()
        if self.label_month_year_PAY.text() != "Май 2006":
            self.btn_Left_PAY.setEnabled(True)
            self.current_month_index = self.period_PAY.click_btn_right(self.current_month_index)
            self.read_pokaz()

    # читает сохраненные данные из базы данных
    def read_pokaz(self):
        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский 00000419

        file_db = open('COMMPAY_DAT.db', 'a')  # открывает файл базы данных
        file_db.close()  # закрывает файл базы данных

        table_count = 'Counters_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы
        table_tariff = 'Tariff_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы
        table_payments = 'Payments_year_' + str(self.comboBox_year_PAY.currentText())  # имя таблицы

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

        read_table = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_count)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table)):
            pred_pokaz = read_table[i]  # показания сохраненного периода
            # print(pred_pokaz)

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_PAY.text() == pred_pokaz[1]:
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

    def btn_save_PAY(self):
        pass
        # self.data = self.create_list_pokaz_schet()  # создает список значений
        # table = 'Pokazanya_year_' + self.data[1].split()[1]  # Имя таблицы ("1")
        # col_name = 'id'  # Имя колонки
        # row_record = self.data[0]  # Имя записи ("1")

        # col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]

        # if row_record in col_id:
        #     self.label_error_PAY.show()
        #     self.label_error_PAY.setText('Такая запись уже существует!')
        #     self.save_yes_or_not()
        # else:
        #     SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, self.data)
        #     self.read_pokaz_schet()
        #
        #     if self.comboBox_month_COU.currentIndex() + 2 != 13:
        #         b = month[self.comboBox_month_COU.currentIndex() + 1]
        #         c = self.comboBox_year_COU.currentText()
        #     else:
        #         b = month[self.comboBox_month_COU.currentIndex() - 11]
        #         c = str(int(self.comboBox_year_COU.currentText()) + 1)
        #
        #     self.label_month_year_COU.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
        #     self.comboBox_month_COU.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
        #     self.comboBox_year_COU.setCurrentText(c)  # устанавливает текущий год ("Год")
        #
        #     self.read_pokaz_schet()

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

    def btn_cancel_PAY(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PAY = CommunalPayment()
    sys.exit(app.exec_())
