# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication

from res.DLL_CLASS_KOMM_ED import *
from res.UIC_CLASS_KOMM_ED import UiWinAdd, NewPlateg

from COMMPAY_UIC import UiWinPayment


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class KommunalPayment(QtWidgets.QWidget, UiWinPayment):
    def __init__(self):
        super(KommunalPayment, self).__init__()

        self.setupUi_CP(self)

        self.period_CP = Period(self.comboBox_month_CP, self.comboBox_year_CP, self.label_month_year_CP)
        self.save_or_CP = Save_OR()

        # ВЫБОР ПЕРИОДА
        selected_period(self.comboBox_month_CP, self.comboBox_year_CP)
        self.comboBox_month_CP.activated.connect(self.label_period)  # месяц
        self.comboBox_year_CP.activated.connect(self.label_period)  # год

        # ТЕКУЩЕГО ПЕРИОДА
        self.current_month_index = month.index(convert_month(dt_month))  # Текущий месяц (int(0))

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_CP.setText(convert_month(dt_month) + " " + dt_year)  # заголовок ("Месяц Год")
        self.comboBox_month_CP.setCurrentIndex(self.current_month_index)  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_CP.setCurrentText(dt_year)  # устанавливает текущий год ("Год")

        self.btn_Left_CP.clicked.connect(self.btn_period_left)  # прокрутка в лево
        self.btn_Right_CP.clicked.connect(self.btn_period_right)  # прокрутка в право

        self.btn_Save_CP.clicked.connect(self.btn_save_cp)
        self.btn_Cancel_CP.clicked.connect(self.btn_cancel_cp)

        self.pay_power = Widget_Payment("Электричество")
        self.g_layout_pay_group.addWidget(self.pay_power, 1, 0, 1, 1)

        self.pay_water = Widget_Payment("Вода")
        self.g_layout_pay_group.addWidget(self.pay_water, 2, 0, 1, 1)

        self.pay_gaz = Widget_Payment("Газ")
        self.g_layout_pay_group.addWidget(self.pay_gaz, 3, 0, 1, 1)

        self.pay_apartment = Widget_Payment("Квартира")
        self.g_layout_pay_group.addWidget(self.pay_apartment, 4, 0, 1, 1)

        # ЧИТАЕМ показания из базы данных
        # self.read_pokaz_schet()

        self.show()

    def label_period(self):
        self.start_period()
        self.current_month_index = self.period_CP.label_sel_period()
        # self.read_pokaz_schet()

    def btn_period_left(self):
        self.start_period()
        if self.label_month_year_CP.text() == "Июнь 2006":
            self.btn_Left_CP.setEnabled(False)
        else:
            self.current_month_index = self.period_ps.click_btn_left(self.current_month_index)
            # self.read_pokaz_schet()

    def btn_period_right(self):
        self.start_period()
        if self.label_month_year_CP.text() != "Май 2006":
            self.btn_Left_CP.setEnabled(True)
            self.current_month_index = self.period_ps.click_btn_right(self.current_month_index)
            # self.read_pokaz_schet()

    def btn_save_cp(self):
        self.data = self.create_list_pokaz_schet()  # создает список значений
        table = 'Pokazanya_year_' + self.data[1].split()[1]  # Имя таблицы ("1")
        col_name = 'id'  # Имя колонки
        row_record = self.data[0]  # Имя записи ("1")

        # col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]

        # if row_record in col_id:
        #     self.label_error_CP.show()
        #     self.label_error_CP.setText('Такая запись уже существует!')
        #     self.save_yes_or_not()
        # else:
        #     SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, self.data)
        #     self.read_pokaz_schet()
        #
        #     if self.comboBox_month_PS.currentIndex() + 2 != 13:
        #         b = month[self.comboBox_month_PS.currentIndex() + 1]
        #         c = self.comboBox_year_PS.currentText()
        #     else:
        #         b = month[self.comboBox_month_PS.currentIndex() - 11]
        #         c = str(int(self.comboBox_year_PS.currentText()) + 1)
        #
        #     self.label_month_year_PS.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
        #     self.comboBox_month_PS.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
        #     self.comboBox_year_PS.setCurrentText(c)  # устанавливает текущий год ("Год")
        #
        #     self.read_pokaz_schet()
        pass

    def save_yes_or_not(self):
        self.save_yn.name_platega()
        self.save_yn.setWindowTitle("Сохранение")

        self.save_yn.lineEdit.close()
        self.save_yn.label_pust.setGeometry(QtCore.QRect(10, 0, 270, 70))
        self.save_yn.label_pust.setText("Вы действительно хотите \n перезаписать показания?")

        self.save_yn.btn_OK.clicked.connect(self.save_yn_btn_ok)
        self.save_yn.btn_OK.setAutoDefault(True)
        self.save_yn.btn_Cancel.clicked.connect(self.save_yn_btn_cancel)

    def save_yn_btn_ok(self):
        table = 'Pokazanya_year_' + self.data[1].split()[1]  # имя таблицы (период)
        col_name = 'id'  # имя колонки
        row_record = self.data[0]  # имя записи

        # SQLite3_Data_Base.sqlite3_delete_record(self.data_base, table, col_name, str(row_record))  # удаляем запись
        # SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, self.data)  # вставляем изменённую запись

        # self.read_pokaz_schet()
        self.label_error_CP.hide()
        self.save_yn.close()

    def save_yn_btn_cancel(self):
        self.label_error_CP.hide()
        self.save_yn.close()

    def btn_cancel_cp(self):
        self.close()

    #     self.period_kp = Period(self.comboBox_month_KP, self.comboBox_year_KP, self.label_month_year_KP)
    #     self.c = Communicate()
    #
    #     current_month = convert_month(dt_month)  # Текущий месяц ("Январь")
    #     current_year = dt_year  # Текущий год ("2020")
    #
    #     self.month_index = month.index(current_month)
    #     self.month_text = month[self.month_index]
    #     self.year_index = int(current_year)
    #
    #     # ВЫБОР ПЕРИОДА
    #     combo_m = self.comboBox_month_KP
    #     combo_y = self.comboBox_year_KP
    #     selected_period(combo_m, combo_y)
    #
    #     # установка ТЕКУЩЕГО ПЕРИОДА
    #     self.label_month_year_KP.setText(current_month + " " + current_year)  # устанавливает заголовок ("Январь 2020")
    #     self.comboBox_month_KP.setCurrentIndex(month.index(current_month))  # устанавливает текущий месяц ("Январь")
    #     self.comboBox_year_KP.setCurrentText(current_year)  # устанавливает текущий год ("2020")
    #
    #     # ВЫБИРАЕМ период
    #     self.comboBox_month_KP.activated.connect(self.label_period)
    #     self.comboBox_year_KP.activated.connect(self.label_period)
    #
    #     self.btn_Left_KP.clicked.connect(self.btn_period_left)
    #     self.btn_Right_KP.clicked.connect(self.btn_period_right)
    #
    #     # режим РЕДАКТИРОВАНИЯ значений
    #     self.checkBox_Edit_KP.setChecked(False)
    #     self.checkBox_Edit_KP.stateChanged.connect(self.read_only)
    #
    #     # подтверждение платежа
    #     self.btn_check_Power.clicked.connect(self.ku)  # check_status
    #     self.btn_check_Water.clicked.connect(self.ku)
    #     self.btn_check_Gaz.clicked.connect(self.ku)
    #
    #     # ДОБАВЛЕНИЕ ПЛАТЕЖА
    #     self.pushButton_add_Plateg_KP.clicked.connect(self.btn_add_plateg)
    #
    #     # СОХРАНЯЕМ показания
    #     self.pushButton_Save_KP.clicked.connect(self.btn_save_kp)
    #
    #     # ЗАКРЫВАЕТ окно ПЛАТЕЖИ
    #     self.pushButton_Cancel_KP.clicked.connect(self.btn_cancel_kp)
    #
    #     # ЧИТАЕТ платежи из базы данных
    #     self.read_kommunal_plateg()
    #
        # self.show()
    #
    # # показывает в заголовке выбранный месяц и год
    # def label_period(self):
    #     self.default_win()
    #     self.month_index = self.period_kp.label_sel_period()
    #     self.read_kommunal_plateg()
    #
    # # прокрутка переиода в лево
    # def btn_period_left(self):
    #     self.default_win()
    #     self.month_index = self.period_kp.click_btn_left(self.month_index)
    #     self.read_kommunal_plateg()
    #
    # # прокрутка переиода в право
    # def btn_period_right(self):
    #     self.default_win()
    #     self.month_index = self.period_kp.click_btn_right(self.month_index)
    #     self.read_kommunal_plateg()
    #
    # # значения по умолчанию
    # def default_win(self):
    #     self.WinPayment.resize(800, 365)
    #     self.WinPayment.setMinimumSize(QtCore.QSize(800, 365))
    #     self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0))
    #
    # # открывает окно "добавление нового платежа"
    # def btn_add_plateg(self):
    #     self.win_add = UiWinAdd()
    #     self.win_add.name_plateg()
    #
    #     if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
    #         win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский  00000419
    #
    #     # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
    #     self.win_add.btn_OK.clicked.connect(self.win_add_name_ok)  # кнопка OK окна ИМЯ
    #     self.win_add.btn_OK.setAutoDefault(True)
    #     self.win_add.lineEdit.returnPressed.connect(self.win_add.btn_OK.click)
    #
    #     self.win_add.btn_Cancel.clicked.connect(self.win_add_name_cancel)  # кнопка CANCEL
    #
    # # кнопка OK окна "ИМЯ нового платежа"
    # def win_add_name_ok(self):
    #     self.name = self.win_add.lineEdit.text()
    #
    #     self.win_add.lineEdit.clear()
    #     self.win_add.close()
    #
    #     self.summ_plat = UiWinAdd()
    #     self.summ_plat.name_plateg()
    #     self.summ_plat.label.setText("Сумма платежа")
    #
    #     if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
    #         win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419
    #
    #     self.summ_plat.btn_OK.clicked.connect(self.win_add_summ_ok)  # кнопка OK окна СУММА
    #     self.summ_plat.btn_OK.setAutoDefault(True)
    #     self.summ_plat.lineEdit.returnPressed.connect(self.summ_plat.btn_OK.click)
    #
    #     self.summ_plat.btn_Cancel.clicked.connect(self.win_add_summ_cancel)
    #
    # # кнопка OK окна "СУММА нового платежа"
    # def win_add_summ_ok(self):
    #     self.sum = self.summ_plat.lineEdit.text()
    #     self.sum_text = text_convert(self.sum)
    #
    #     self.create_plat(self.name, self.sum_text)
    #
    #     # возможно удаление после того как был создан доп. плат.
    #     self.new_p.btn_del_Plat.clicked.connect(self.btn_del_plateg)
    #     self.new_p.btn_del_Plat.clicked.connect(self.new_p.deleteLater)
    #
    #     self.summ_plat.lineEdit.clear()
    #     self.summ_plat.close()
    #
    # def btn_del_plateg(self):
    #     self.frame_h -= 35
    #     self.win_h -= 35
    #     self.win_h_del = self.win_h - 35
    #
    #     self.WinPayment.setMinimumSize(QtCore.QSize(800, self.win_h))
    #     self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, self.frame_h))
    #     self.WinPayment.resize(800, self.win_h_del)
    #
    # def create_plat(self, name, summ):
    #     self.new_p = NewPlateg(name, summ)
    #     self.gridLayout.addWidget(self.new_p)
    #
    #     self.frame_h += 35
    #     self.win_h += 35
    #
    #     self.WinPayment.setMinimumSize(QtCore.QSize(800, self.win_h))
    #     self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, self.frame_h))
    #
    #     self.dop_plategi[self.name] = float(self.sum), 0, 0
    #     self.dict_pole[self.name] = float(self.sum)
    #     self.plategi_sum += float(self.sum)
    #     self.itog_sum(self.plategi_sum)
    #
    #     self.WinPayment.setTabOrder(None, self.pushButton_add_Plateg_KP)
    #
    # # кнопка CANCEL окна "ИМЯ нового платежа"
    # def win_add_name_cancel(self):
    #     self.win_add.lineEdit.clear()
    #     self.win_add.close()
    #
    # # кнопка CANCEL окна "СУММА нового платежа"
    # def win_add_summ_cancel(self):
    #     self.summ_plat.lineEdit.clear()
    #     self.summ_plat.close()
    #
    # def ku(self):
    #     source = self.sender()
    #     print('Привет')
    #
    #     if source.text() == 'Power':
    #         print('Power')
    #         # self.col.setRed(val)
    #     elif source.text() == 'Water':
    #         print('Water')
    #     elif source.text() == 'Gaz':
    #         print('Gaz')
    #
    # # def check_status(self, pressed):
    # #     source = self.sender()
    # #
    # #     if pressed:
    # #         val = str(1)
    # #     else:
    # #         val = str(0)
    # #
    # #     print('Power' + val)
    # #     print('Water' + val)
    # #     print('Gaz' + val)
    # #
    # #     if source.text() == 'Power':
    # #         print('Power' + val)
    # #         # self.col.setRed(val)
    # #     elif source.text() == 'Water':
    # #         print('Water' + val)
    # #     elif source.text() == 'Gaz':
    # #         print('Gaz' + val)
    # #         # self.col.setGreen(val)
    # #     # else:
    # #     #     self.col.setBlue(val)
    #
    # # читаем сохраненые данные из базы данных
    # def read_kommunal_plateg(self):  # читаем данные из базы данных
    #     self.data_base = 'Komunal.db'
    #     self.table_pokaz = 'Pokazanya_year_' + str(self.comboBox_year_KP.currentText())
    #     self.table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
    #     self.heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'
    #     self.col_name = 'id'
    #
    #     self.plategi_trf = {}  # словарь только сохраненных значений тарифов
    #     self.dop_plategi = {}  # словарь всех ПЛАТЕЖЕЙ
    #     self.plategi_sum = 0  # общая сумма всех платежей
    #
    #     # self.year = self.comboBox_year_KP.currentText()  # "ГОД" нужен для функции denominacia
    #
    #     self.win_h = 365
    #     self.frame_h = 0
    #
    #     self.WinPayment.resize(800, 365)
    #     self.WinPayment.setMinimumSize(QtCore.QSize(800, 365))
    #     self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0))
    #     self.checkBox_Edit_KP.setChecked(False)
    #
    #     # очищаем поля окна ПЛАТЕЖИ
    #     self.dict_pole = {
    #         'Электричество': [self.lineEdit_sum_Power, self.lineEdit_kol_Power, self.lineEdit_trf_Power],
    #         'Вода': [self.lineEdit_sum_Water, self.lineEdit_kol_Water, self.lineEdit_trf_Water],
    #         'Газ': [self.lineEdit_sum_Gaz, self.lineEdit_kol_Gaz, self.lineEdit_trf_Gaz]}
    #
    #     self.list_pole_trf = [self.lineEdit_trf_Power, self.lineEdit_trf_Water, self.lineEdit_trf_Gaz,
    #                           self.label_ERROR_KP, self.label_OK_KP, self.lineEdit_IS_sum]
    #
    #     self.clear_win()
    #
    #     self.create_base(self.data_base, self.table_plateg, self.heading)
    #
    #     self.read_base_pokaz(self.data_base, self.table_pokaz)
    #     self.read_base_plateg_trf(self.data_base, self.table_plateg, self.col_name)
    #     self.read_base_plateg_dop(self.data_base, self.table_plateg)
    #
    #     self.all_summ()
    #
    # def clear_win(self):
    #     for i in self.dict_pole.values():
    #         for j in i:
    #             j.clear()
    #
    #     for i in self.list_pole_trf:
    #         i.clear()
    #
    #     self.checkBox_Edit_KP.show()
    #
    #     clear_layout(self.gridLayout)  # удаляем все доп. платежи
    #
    # def create_base(self, base, table, heading):
    #     file_db = open('Komunal.db', 'a')
    #     file_db.close()
    #
    #     SQLite3_Data_Base.sqlite3_create_tbl(base, table, heading)  # создаем базу данных в случаи ее отсутствия
    #
    # # читаем таблицу ПОКАЗАНИЙ счетчиков из базы данных
    # def read_base_pokaz(self, base, table):
    #     try:
    #         read_table_CP = SQLite3_Data_Base.sqlite3_read_data(base, table)
    #         read_table_CP = read_table_CP[0]
    #
    #         for i in range(len(read_table_CP)):
    #             if read_table_CP[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1:
    #                 pred_pokaz = read_table_CP[i]
    #
    #                 self.lineEdit_kol_Power.setText(str(pred_pokaz[14]))
    #                 self.lineEdit_kol_Water.setText(str(pred_pokaz[17]))
    #                 self.lineEdit_kol_Gaz.setText(str(pred_pokaz[18]))
    #
    #     except sqlite3.OperationalError:
    #         self.checkBox_Edit_KP.show()
    #
    # # читаем таблицу ПЛАТЕЖЕЙ (ищим значения тарифов)
    # def read_base_plateg_trf(self, base, table, col):
    #     # проверяем существует ли такая запись в таблице ПЛАТЕЖЕЙ, если ДА то помечаем галочкой
    #     if self.comboBox_month_KP.currentIndex() + 1 in SQLite3_Data_Base.sqlite3_read_data(base, table, col)[0]:
    #         self.label_OK_KP.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))
    #
    #     # читаем таблицу ПЛАТЕЖЕЙ из базы данных (ищим значения тарифов)
    #     try:
    #         # если нет записи (только январь)
    #         if self.comboBox_month_KP.currentIndex() + 1 not in SQLite3_Data_Base.sqlite3_read_data(
    #                 base, table, "id")[0] and month[self.comboBox_month_KP.currentIndex()] == "Январь":
    #             # таблица из предыдущего года
    #             table_plateg_jan = 'Plategi_year_' + str(int(self.comboBox_year_KP.currentText()) - 1)
    #             read_table_last = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_plateg_jan)[0]
    #             for a in read_table_last:  # значения тарифов из декабрьской таблицы
    #                 if a[0] == self.comboBox_month_KP.currentIndex() + 12:
    #                     self.plategi_trf[a[2]] = a[5]
    #         # если нет записи (любой месяц кроме января)
    #         elif self.comboBox_month_KP.currentIndex() + 1 not in SQLite3_Data_Base.sqlite3_read_data(
    #                 base, table, "id")[0] and month[self.comboBox_month_KP.currentIndex()] != "Январь":
    #             # таблица из текущего года
    #             table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
    #             read_table_last = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_plateg)[0]
    #             for a in read_table_last:  # значения тарифов предыдущего периода
    #                 if a[0] == self.comboBox_month_KP.currentIndex():
    #                     self.plategi_trf[a[2]] = a[5]
    #         else:  # если есть запись (любой месяц)
    #             # таблица из текущего года
    #             table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
    #             read_table_last = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table_plateg)[0]
    #             for a in read_table_last:  # значения тарифов сохраненного периода
    #                 if a[0] == self.comboBox_month_KP.currentIndex() + 1:
    #                     self.plategi_trf[a[2]] = a[5]
    #
    #         # устанавливаем значения тарифов в поля окна
    #         for j, a in zip(self.plategi_trf.values(), self.list_pole_trf[:3]):
    #             a.setText(str(j))
    #
    #         # вычисляем значения суммы для наших счетчиков согласно тарифов
    #         # и заносим эти значения в поля окна и в словарь платежей
    #         for p, v in self.dict_pole.items():
    #             pl_sum = float(v[1].text()) * float(v[2].text())  # вычисляем значения суммы
    #             list_pl = pl_sum, int(v[1].text()), float(v[2].text())
    #             self.dop_plategi[p] = list_pl  # заносим значения в словарь платежей
    #             den = denomination(self.comboBox_year_KP.currentText(), pl_sum)
    #             v[0].setText(den + " руб")  # заносим значения в поля окна
    #
    #     except sqlite3.OperationalError:
    #         self.checkBox_Edit_KP.show()
    #     except ValueError:
    #         self.checkBox_Edit_KP.show()
    #
    # # читаем таблицу ПЛАТЕЖЕЙ из базы данных (имя и значение доп.платежа)
    # def read_base_plateg_dop(self, base, table):
    #     read_table_KP = SQLite3_Data_Base.sqlite3_read_data(base, table)[0]
    #
    #     for i in read_table_KP:  # имя и значения доп.платежа сохраненного периода
    #         year = self.comboBox_year_KP.currentText()
    #
    #         if i[0] == self.comboBox_month_KP.currentIndex() + 1:
    #
    #             self.dop_plategi[i[2]] = i[3]  # заносим в словарь
    #
    #         try:
    #             if i[2] == 'Электричество':
    #                 self.lineEdit_trf_Power.setText(str(self.plategi_trf.get(i[2], "")))
    #                 self.sum_platega(self.dict_pole, i[2], year)
    #             elif i[2] == 'Вода':
    #                 self.lineEdit_trf_Water.setText(str(self.plategi_trf.get(i[2], "")))
    #                 self.sum_platega(self.dict_pole, i[2], year)
    #             elif i[2] == 'Газ':
    #                 self.lineEdit_trf_Gaz.setText(str(self.plategi_trf.get(i[2], "")))
    #                 self.sum_platega(self.dict_pole, i[2], year)
    #
    #         except ValueError:
    #             self.checkBox_Edit_KP.show()
    #
    # # вычисляем общую сумму всех платежей
    # def all_summ(self):
    #     for i, j in self.dop_plategi.items():
    #         self.plategi_sum += float(j[0]) if type(j) == tuple else float(j)
    #
    #         if i == 'Электричество':
    #             continue
    #         elif i == 'Вода':
    #             continue
    #         elif i == 'Газ':
    #             continue
    #         else:
    #             self.frame_h += 35
    #             self.win_h += 35
    #
    #             self.WinPayment.setMinimumSize(QtCore.QSize(800, self.win_h))
    #             self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, self.frame_h))
    #
    #             summ = text_convert(str(float(j)))
    #             self.new_p = NewPlateg(i, summ)
    #             self.gridLayout.addWidget(self.new_p)
    #
    #             self.dop_plategi[i] = (float(j), 0, 0)
    #             self.dict_pole[i] = self.new_p.lineEdit_sum_Plat
    #             self.new_p.lineEdit_sum_Plat.setText(text_convert(str(j)) + " руб")
    #
    #             # возможно удаление после того как был создан доп. плат.
    #             self.new_p.btn_del_Plat.clicked.connect(self.btn_del_plateg)
    #             self.new_p.btn_del_Plat.clicked.connect(self.new_p.deleteLater)
    #
    #         self.new_p.lineEdit_sum_Plat.textEdited[str].connect(
    #             lambda: self.text_editing(self.new_p.lineEdit_sum_Plat))
    #
    #     self.itog_sum(self.plategi_sum)
    #
    # # функция вычисляет сумму платежа и заносит значение в поле сумма
    # def sum_platega(self, pole, plat, year):
    #     v = pole.get(plat)
    #     pl_sum = float(v[1].text()) * float(v[2].text())
    #     list_pl = pl_sum, int(v[1].text()), float(v[2].text())
    #     self.dop_plategi[plat] = list_pl
    #     den = denomination(year, pl_sum)
    #     v[0].setText(den + " руб")
    #
    # # вычисляем итоговою сумму платежей
    # def itog_sum(self, plategi_sum):
    #     if self.plategi_sum > 0:
    #         year = self.comboBox_year_KP.currentText()
    #         den = denomination(year, cash=plategi_sum)
    #         self.lineEdit_IS_sum.setText(den + " руб")
    #
    # # включение режима редактирования
    # def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
    #     if self.checkBox_Edit_KP.isChecked():
    #         self.lineEdit_trf_Power.setReadOnly(False)
    #         self.lineEdit_trf_Water.setReadOnly(False)
    #         self.lineEdit_trf_Gaz.setReadOnly(False)
    #     else:
    #         self.lineEdit_trf_Power.setReadOnly(True)
    #         self.lineEdit_trf_Water.setReadOnly(True)
    #         self.lineEdit_trf_Gaz.setReadOnly(True)
    #
    #     self.lineEdit_trf_Power.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Power))
    #     self.lineEdit_trf_Water.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Water))
    #     self.lineEdit_trf_Gaz.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Gaz))
    #
    # # режим редактирования
    # def text_editing(self, lineEdit_sum):
    #     try:
    #         if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
    #             win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419
    #
    #         self.label_ERROR_KP.clear()
    #         self.checkBox_Edit_KP.show()
    #         year = self.comboBox_year_KP.currentText()
    #
    #         if lineEdit_sum == self.lineEdit_sum_Power:
    #             self.sum_platega(self.dict_pole, 'Электричество', year)
    #         elif lineEdit_sum == self.lineEdit_sum_Water:
    #             self.sum_platega(self.dict_pole, 'Вода', year)
    #         elif lineEdit_sum == self.lineEdit_sum_Gaz:
    #             self.sum_platega(self.dict_pole, 'Газ', year)
    #         elif lineEdit_sum == self.new_p.lineEdit_sum_Plat:
    #             v = self.dict_pole.get(self.new_p.label_Plat.text())
    #
    #             pl_sum = float(v.text())
    #             list_pl = pl_sum, 0, 0
    #             self.dop_plategi[self.new_p.label_Plat.text()] = list_pl
    #
    #             def ok():
    #                 den_ok = denomination(year, pl_sum)
    #                 v.setText(den_ok + " руб")
    #
    #             v.returnPressed.connect(ok)
    #
    #         self.plategi_sum = 0
    #
    #         for i, j in self.dop_plategi.items():
    #             self.plategi_sum += float(j[0]) if type(j) == tuple else float(j)
    #
    #         self.itog_sum(self.plategi_sum)
    #
    #     except ValueError:
    #         self.checkBox_Edit_KP.hide()
    #         self.label_ERROR_KP.setText('Должно быдь значение!')
    #
    # # подготовка данных к сохранению
    # def create_list_plateg_kommun(self):
    #     data = []
    #
    #     id_row = self.comboBox_month_KP.currentIndex() + 1
    #     select_period = self.comboBox_month_KP.currentText() + " " + self.comboBox_year_KP.currentText()
    #
    #     for i, j in self.dop_plategi.items():
    #         data.append((id_row, select_period, i, *j))
    #
    #     return data
    #
    # # кнопка сохранения данных
    # def btn_save_kp(self):
    #     data = self.create_list_plateg_kommun()
    #
    #     table = 'Plategi_year_' + data_convert(data[1])
    #
    #     col_name = 'id'  # Имя колонки
    #     row_record = str(data[0][0])  # Имя записи
    #     a = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]
    #
    #     try:
    #         if int(row_record) in a:
    #             self.save_yes_or_not()
    #         else:
    #             for data_i in data:
    #                 pass
    #                 SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, data_i)
    #
    #             self.read_kommunal_plateg()
    #
    #         self.btn_period_right()
    #
    #         # if self.comboBox_month_KP.currentIndex() + 2 != 13:
    #         #     b = month[self.comboBox_month_KP.currentIndex() + 1]
    #         #     c = self.comboBox_year_KP.currentText()
    #         # else:
    #         #     b = month[self.comboBox_month_KP.currentIndex() - 11]
    #         #     c = str(int(self.comboBox_year_KP.currentText()) + 1)
    #         #
    #         # self.label_month_year_KP.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
    #         # self.comboBox_month_KP.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
    #         # self.comboBox_year_KP.setCurrentText(c)  # устанавливает текущий год ("Год")
    #
    #     except sqlite3.IntegrityError:
    #         self.checkBox_Edit_KP.hide()
    #         self.label_ERROR_KP.setText('Такая запись уже существует!')
    #
    # # режим перезаписи сохраненных данных
    # def save_yes_or_not(self):
    #     self.save_yn = UiWinAdd()
    #     self.save_yn.name_plateg()
    #     self.save_yn.setWindowTitle("Сохранение")
    #     self.save_yn.lineEdit.close()
    #     self.save_yn.label.setGeometry(QtCore.QRect(10, 0, 270, 70))
    #     self.save_yn.label.setText("Вы действительно хотите \n презаписать эту запись?")
    #
    #     self.save_yn.btn_OK.clicked.connect(self.btn_ok_save_yn)
    #     self.save_yn.btn_OK.setAutoDefault(True)
    #     self.save_yn.btn_Cancel.clicked.connect(self.btn_cancel_save_yn)
    #
    # # перезапись сохраненных данных
    # def btn_ok_save_yn(self):
    #     data = self.create_list_plateg_kommun()  # список данных для записи
    #     table = 'Plategi_year_' + data_convert(data[1])  # имя таблицы (период)
    #     col_name = 'id'  # имя колонки
    #     row_record = str(data[0][0])  # имя записи
    #
    #     for data_i in data:
    #         SQLite3_Data_Base.sqlite3_delete_record(self.data_base, table, col_name, row_record)
    #         SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, data_i)
    #
    #     self.read_kommunal_plateg()
    #
    #     self.save_yn.close()
    #
    # # кнопка отмены перезаписи
    # def btn_cancel_save_yn(self):
    #     self.save_yn.close()
    #
    # # кнопка закрытия окна "Коммунальные платежи"
    # def btn_cancel_kp(self):
    #     self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_KP = KommunalPayment()
    sys.exit(app.exec_())
