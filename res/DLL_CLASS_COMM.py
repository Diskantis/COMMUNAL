# -*- coding: utf-8 -*-

import re
import sqlite3
import datetime

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget

from res.UIC_CLASS_COMM import UiWinAdd, Ui_Widget_Payment

dt_day = datetime.datetime.now().strftime("%d")  # Текущий день (str "30")
dt_month = datetime.datetime.now().strftime("%m")  # Текущий месяц (str "01")
dt_year = datetime.datetime.now().strftime("%Y")  # Текущий год (str "2020")

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
         'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


def convert_month(input_month):  # Конвертирует текущий месяц из строки "01" в слово "Январь"
    out_month = int(input_month)  # "01" = 1
    for i in range(1, len(month) + 1):
        if i == out_month:
            out_month = month[i - 1]
    return out_month  # "Январь"


def selected_period(combo_m, combo_y):
    combo_m.clear()
    combo_m.addItems(month)  # Выбор месяц в comboBox_month_KP

    combo_y.clear()
    last_year = 2023
    if dt_month == "12":
        last_year += 1
    for year_num in range(2006, last_year):  # Выбор года в comboBox_year_KP
        combo_y.addItem('%d' % year_num)


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clear_layout(child.layout())


def denomination(year_in, month_in, cash):
    year_in = int(year_in)
    if year_in <= 2016 and month_in + 1 < 6:
        den_cash = text_convert(str(int(round(cash, 0))))
    else:
        den_cash = text_convert(str('{:.2f}'.format(float(cash))))  # (str(float(round(cash, 2))))
    return den_cash


def text_convert(string):
    if " " in string:
        res = re.sub(r'\s+', '', string, flags=re.UNICODE)
    else:
        res = re.sub(r'\d(?=(?:\d{3})+(?!\d))', r'\g<0> ', string)
    return res


def text_conv_to_num(string):
    res = re.sub(r'\s+', '', string, flags=re.UNICODE)
    return res


def num_conv_to_text(string):
    res = re.sub(r'\d(?=(?:\d{3})+(?!\d))', r'\g<0> ', string)
    return res


def center(a):
    qr = a.geometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    a.move(qr.topLeft())


def str_list(val):  # функция для преобразования self.status
    if isinstance(val, str):
        val = list(map(int, list(val.split())))
    elif isinstance(val, list):
        val = " ".join(map(str, val))
    return val


def payment_checked(list_pay, list_status):
    for j, a in zip(list_pay, list_status):
        if a == 0:
            j.setChecked(False)
        else:
            j.setChecked(True)


def data_convert(data):
    a = data[1]
    b = a.split()
    c = b[1]
    return c


# НОВЫЙ ПЛАТЕЖ
class Widget_Payment(QtWidgets.QWidget, Ui_Widget_Payment):
    def __init__(self, name, color):
        super(Widget_Payment, self).__init__()

        self.setupUi(self, color)
        self.btn_check.setText(name)


# ВЫБОР ПЕРИОДА
class Period:
    def __init__(self, c_box_month, c_box_year, label_month_year):
        self.month = month
        self.comboBox_month = c_box_month
        self.comboBox_year = c_box_year
        self.label_month_year = label_month_year

    def label_sel_period(self):  # показывает в заголовке выбранный месяц и год
        m_sel = self.comboBox_month.currentText()  # выбранный в comboBox месяц
        y_sel = self.comboBox_year.currentText()  # выбранный в comboBox год
        self.label_month_year.setText(m_sel + " " + y_sel)  # заголовок ("Январь 2020")
        month_index = self.month.index(m_sel)
        return month_index

    def click_btn_left(self, month_index):  # прокрутка периода в лево
        if month_index > 0:
            month_index = month_index - 1  # self.comboBox_month.currentIndex()
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = self.comboBox_year.currentText()
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        else:
            month_index = 11
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = str(int(self.comboBox_year.currentText()) - 1)
            self.comboBox_year.setCurrentText(self.year_index)
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        return month_index

    def click_btn_right(self, month_index):  # прокрутка периода в право
        if month_index < 11:
            month_index = month_index + 1  # self.comboBox_month.currentIndex()
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = self.comboBox_year.currentText()
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        else:
            month_index = 0
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = str(int(self.comboBox_year.currentText()) + 1)
            self.comboBox_year.setCurrentText(self.year_index)
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        return month_index


class Save_OR:
    def save_yes_or_not(self, data_base, data, label_error):
        self.save_yn = UiWinAdd()
        self.save_yn.name_payment()
        self.save_yn.setWindowTitle("Перезапись")

        self.save_yn.lineEdit.deleteLater()

        if data[2] == "Counters":
            self.name_table = "Показаниями счетчиков"
        elif data[2] == "Tariff":
            self.name_table = "Тарифами"
        elif data[2] == "Payments":
            self.name_table = "Платежами"

        font = QtGui.QFont("Times", 10, 75)
        self.save_yn.label.setFont(font)
        self.save_yn.label.setText("Вы действительно хотите \n перезаписать таблицу \n с " + self.name_table + " ?")

        self.save_yn.add_pay_btn_OK.clicked.connect(lambda: self.save_yn_btn_ok(data_base, data, label_error))
        self.save_yn.add_pay_btn_OK.setAutoDefault(True)
        self.save_yn.add_pay_btn_Cancel.clicked.connect(lambda: self.save_yn_btn_cancel(label_error))

    def save_yn_btn_ok(self, data_base, data, label_error):
        data = data  # список данных для записи

        table = data[2] + '_year_' + data[1].split()[1]  # имя таблицы (период)
        col_name = 'id'  # имя колонки
        row_record = str(data[0])  # имя записи

        data.remove(data[2])  # Удаляем имя таблицы из списка "Tariff"

        SQLite3_Data_Base.sqlite3_delete_record(data_base, table, col_name, row_record)
        SQLite3_Data_Base.sqlite3_insert_data(data_base, table, data)

        label_error.hide()
        self.save_yn.close()

    def save_yn_btn_cancel(self, label_error):
        label_error.hide()
        self.save_yn.close()


class SQLite3_Data_Base:
    @staticmethod
    def sqlite3_create_tbl(data_base, table, heading):
        """Метод для создания базы данных и таблицы в ней
           data_base - имя базы данных
           table - имя таблицы
           heading - () кортеж заголовков столбцов: heading = ('ID integer primary key , Month_year text,
                                                                Pre_PW integer)
        """

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        # создаем таблицу в базе данных если таблицы не существует
        sql = 'CREATE TABLE IF NOT EXISTS ' + table + '(' + heading + ')'
        cur.execute(sql)

        # классический вариант создания таблицы
        # sql = '''CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, INCOME FLOAT)'''
        # cur.execute(sql)

        con.commit()  # подтверждаем изменения
        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

    @staticmethod
    def sqlite3_delete_tbl(data_base, table):
        """Функция для удаления таблицы из базы данных с указанием имени таблицы
           data_base - имя базы данных
           table - имя таблицы
        """

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        sql = 'DROP TABLE IF EXIST ' + table
        cur.execute(sql)

        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

    @staticmethod
    def sqlite3_insert_data(data_base, table, data):
        """Метод для внесения данных в таблицу
           data_base - имя базы данных
           table - имя таблицы
           data - [] список данных
        """

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        a = '?, ' * (len(data) - 1) + '?'

        sql = 'INSERT INTO ' + table + ' VALUES(' + a + ')'
        cur.execute(sql, data)

        con.commit()  # подтверждаем изменения
        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

    @staticmethod
    def sqlite3_read_data(data_base, table, col_name=None):
        """Метод для чтения данных из таблицы (колонки или колонок)
           data_base - имя базы данных
           table - имя таблицы
           col_name - имя колонки
        """

        con = sqlite3.connect(data_base)  # # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        query_columns = 'PRAGMA table_info(' + table + ')'  # возвращает
        cur.execute(query_columns)
        columns_description = cur.fetchall()
        columns_names = []

        for column in columns_description:
            columns_names.append(column[1])

        if col_name is None:
            query = 'SELECT * FROM ' + table
            cur.execute(query)
            data = cur.fetchall()
        else:
            query = 'SELECT ' + col_name + ' FROM ' + table
            cur.execute(query)
            data = cur.fetchall()
            new_data = []
            for element in data:
                new_data.append(element[0])
            data = new_data
            del new_data

        return data

    @staticmethod
    def sqlite3_read_sort(data_base, table, cols_name, sort_col):
        """Метод для чтения из таблицы выбранной базы данных с сортировкой по имени колонки"""

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        # делаем запрос к базе данных
        query = 'SELECT ' + cols_name + ' FROM ' + table + ' ORDER BY ' + sort_col
        cur.execute(query)
        data = cur.fetchall()  # помещаем считаные записи из запроса в переменную data

        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

        return data

    @staticmethod
    def sqlite3_delete_record(data_base, table, col_name, row_record):
        """Функция для удаления записи в указанной таблице, указанной базы данных
        по названию колонки (id_column) и значению ячейки (record_id) в указанной колонке"""

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        # создаем запрос на удаление записи по ключу record_id из колонки ключей id_column
        query = 'DELETE FROM ' + table + ' WHERE ' + col_name + ' = ' + "'" + row_record + "'"
        cur.execute(query)

        con.commit()  # подтверждаем изменения
        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

    @staticmethod
    def sqlite3_update_record(data_base, table, col_name, row_record, param_col, param_val):
        """Функция для обновления значения/записи в указанной таблице, указанной базы данных
        в таблице (table) в записи ((col_name) колонка (row_record) запись) ROW заменить значение в (param_col) COL
        на значение (param_val)"""

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        # создаем запрос на обновление значения/записи
        query = 'UPDATE ' + table + ' SET ' + param_col + ' = ' + str(param_val) + ' WHERE ' + col_name + ' = ' + \
                "'" + str(row_record) + "'"
        print(query)
        cur.execute(query)

        con.commit()  # подтверждаем изменения
        cur.close()  # удаляем курсор
        con.close()  # разрываем соединение с базой

    @staticmethod
    def sqlite3_inner_join(data_base, table_1, table_2, col_name_tb_1, col_name_tb_2, cols_out=None):
        """Функция для объединения нескольких таблиц"""

        con = sqlite3.connect(data_base)  # подключаемся к базе данных
        cur = con.cursor()  # создаем объект курсора

        if cols_out is None:
            sql = 'SELECT * FROM ' + table_1 + ' INNER JOIN ' + table_2 + \
                  ' ON ' + col_name_tb_1 + ' = ' + col_name_tb_2 + "'"
        else:
            sql = 'SELECT ' + cols_out + ' FROM ' + table_1 + ' INNER JOIN ' + table_2 + \
                  ' ON ' + col_name_tb_1 + ' = ' + col_name_tb_2 + "'"

        cur.execute(sql)
        data = cur.fetchall()
        return data
