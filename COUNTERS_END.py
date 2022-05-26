# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction

from res.DLL_CLASS_COMM import dt_month, dt_year, month, convert_month, selected_period, \
                               Period, Save_OR, SQLite3_Data_Base
from COUNTERS_UIC import UiWinCounters


# ОКНО ПОКАЗАНИЯ СЧЕТЧИКОВ
class Counters(QtWidgets.QWidget, UiWinCounters):
    def __init__(self):
        super(Counters, self).__init__()

        self.setupUi_COU(self)
        self.data_base = 'COMMPAY_DAT.db'  # имя базы данных

        self.period_COU = Period(self.comboBox_month_COU, self.comboBox_year_COU, self.label_month_year_COU)

        # ВЫБОР ПЕРИОДА
        selected_period(self.comboBox_month_COU, self.comboBox_year_COU)
        self.comboBox_month_COU.activated.connect(self.label_period)  # месяц
        self.comboBox_year_COU.activated.connect(self.label_period)  # год

        # ТЕКУЩЕГО ПЕРИОДА
        self.current_month_index = month.index(convert_month(dt_month))  # Текущий месяц (int(0))

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_COU.setText(convert_month(dt_month) + " " + dt_year)  # заголовок ("Месяц Год")
        self.comboBox_month_COU.setCurrentIndex(self.current_month_index)  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_COU.setCurrentText(dt_year)  # устанавливает текущий год ("Год")

        self.btn_Left_COU.clicked.connect(self.btn_period_left)  # прокрутка в лево
        self.btn_Right_COU.clicked.connect(self.btn_period_right)  # прокрутка в право

        self.win_pole = [self.lineEdit_pred_P, self.lineEdit_post_P,
                         self.lineEdit_pred_W1, self.lineEdit_post_W1,
                         self.lineEdit_pred_W2, self.lineEdit_post_W2,
                         self.lineEdit_pred_W3, self.lineEdit_post_W3,
                         self.lineEdit_pred_W4, self.lineEdit_post_W4,
                         self.lineEdit_pred_G, self.lineEdit_post_G,
                         self.label_month_ras_P,
                         self.label_month_ras_WC, self.label_month_ras_WH, self.label_month_ras_W,
                         self.label_month_ras_G,
                         self.label_error_COU, self.label_GL_V_1_COU, self.label_GL_V_2_COU]

        for a in self.win_pole[:12]:
            a.customContextMenuRequested.connect(self.context_menu)

        self.menuLine = QAction("Редактирование", self)
        font = QtGui.QFont("Times", 10, 75)
        self.menuLine.setFont(font)
        self.menuLine.triggered.connect(self.editable)

        self.btn_Save_COU.clicked.connect(self.btn_save_COU)
        self.btn_Cancel_COU.clicked.connect(self.btn_cancel_COU)

        # ЧИТАЕМ показания из базы данных
        self.read_data_counters()

        self.show()

    def context_menu(self, pos):
        menu = QtWidgets.QMenu(self)
        menu.setStyleSheet("border-bottom: 0px; selection-color: rgb(0, 0, 0); color: rgb(209, 209, 217);")
        menu.addAction(self.menuLine)
        menu.exec_(self.sender().mapToGlobal(pos))

    def editable(self):
        self.focusWidget().selectAll()
        for a in self.win_pole[:12]:
            a.setReadOnly(False)

    def start_period(self):
        if self.label_month_year_COU.text() == 'Декабрь 2006' and self.comboBox_month_COU.count() == 12 \
                or int(self.comboBox_year_COU.currentText()) == 2006 and self.comboBox_month_COU.currentIndex() <= 11 \
                and self.comboBox_month_COU.count() == 12:
            self.comboBox_month_COU.clear()
            self.comboBox_month_COU.addItems(month[5:12])
        elif self.label_month_year_COU.text() == 'Декабрь 2006' and self.comboBox_month_COU.count() == 7 \
                or int(self.comboBox_year_COU.currentText()) >= 2007 and self.comboBox_month_COU.currentIndex() >= 0 \
                and self.comboBox_month_COU.count() == 7:
            self.comboBox_month_COU.clear()
            self.comboBox_month_COU.addItems(month)

    def label_period(self):
        self.start_period()
        self.current_month_index = self.period_COU.label_sel_period()
        self.read_data_counters()

    def btn_period_left(self):
        self.start_period()
        if self.label_month_year_COU.text() == "Июнь 2006":
            self.btn_Left_COU.setEnabled(False)
        else:
            self.current_month_index = self.period_COU.click_btn_left(self.current_month_index)
            self.read_data_counters()

    def btn_period_right(self):
        self.start_period()
        if self.label_month_year_COU.text() != "Май 2006":
            self.btn_Left_COU.setEnabled(True)
            self.current_month_index = self.period_COU.click_btn_right(self.current_month_index)
            self.read_data_counters()

    def keyPressEvent(self, event):  # отключает режим редактирования по нажатию клавиши Esc
        if event.key() == Qt.Key_Escape:
            if month.index(self.label_month_year_COU.text().split()[0]) + 1 in \
                    SQLite3_Data_Base.sqlite3_read_data(
                        self.data_base, 'Counters_year_' + str(self.comboBox_year_COU.currentText()), 'id')[0]:
                for a in self.win_pole[:17]:
                    a.setReadOnly(True)
            else:
                for a in self.win_pole[:12:2]:
                    a.setReadOnly(True)
        event.accept()

    # читает сохраненные данные из базы данных
    def read_data_counters(self):
        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский 00000419

        file_db = open('COMMPAY_DAT.db', 'a')  # открывает файл базы данных
        file_db.close()  # закрывает файл базы данных
        table = 'Counters_year_' + str(self.comboBox_year_COU.currentText())  # имя таблицы
        col_name = 'id'  # Имя колонки

        # заголовок атрибутов таблицы
        heading = ('id integer primary key , month_year text,'
                   'Pred_PW integer, Actual_PW integer, '
                   'Pred_WA_1 integer, Actual_WA_1 integer, Pred_WA_2 integer, Actual_WA_2 integer, '
                   'Pred_WA_3 integer, Actual_WA_3 integer, Pred_WA_4 integer, Actual_WA_4 integer, '
                   'Pred_GZ integer, Actual_GZ integer')

        # создает таблицу в базе данных, это нужно если таблица отсутствуют
        SQLite3_Data_Base.sqlite3_create_tbl(self.data_base, table, heading)

        for i in self.win_pole:  # очищает поля окна ПОКАЗАНИЯ СЧЕТЧИКОВ
            i.clear()

        # проверят есть ли в таблице запись на такой месяц, если есть то отмечает галочкой
        if month.index(self.label_month_year_COU.text().split()[0]) + 1 in \
                SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]:
            self.label_GL_V_1_COU.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
            self.label_GL_V_2_COU.setPixmap(QtGui.QPixmap("res/img/Galochka.png"))
            for n in self.win_pole[:17]:
                n.setReadOnly(True)
        else:
            for n in self.win_pole[1:12:2]:
                n.setReadOnly(False)

        # проверят не является ли выбранный месяц январем (если да то читает таблицу за предыдущий год)
        if not SQLite3_Data_Base.sqlite3_read_data(self.data_base, table)[0] and \
                month[self.comboBox_month_COU.currentIndex()] == "Январь":
            table = 'Counters_year_' + str(int(self.comboBox_year_COU.currentText()) - 1)

        # читаем таблицу, получаем список строк значений
        read_table = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table)[0]

        # ищем если в таблице значение для выбранного периода (месяц, год)
        for i in range(len(read_table)):
            pred_pokaz = read_table[i]  # показания сохраненного периода

            # если лейбл "Январь 2021" совпадает со значением в таблице "Январь 2021"
            if self.label_month_year_COU.text() == pred_pokaz[1]:
                # присваиваем полям значения выбранного периода из сохраненной таблицы
                for a, b in zip(self.win_pole[:12], range(2, 14)):  # range = heading поля с 2 по 13
                    a.setText(str(pred_pokaz[b]))
                break
            else:  # если значения не совпадают (берем значение "ПОСЛЕДНЕЕ" из предыдущего месяца)
                pred_month = month[self.comboBox_month_COU.currentIndex() - 1]
                if pred_month in pred_pokaz[1]:
                    # присваиваем полям "ПРЕДЫДУЩИЕ", значения из сохраненной таблицы
                    for c, d in zip(self.win_pole[:11:2], range(3, 14, 2)):
                        c.setText(str(pred_pokaz[d]))
                    # а полям "ПОСЛЕДНЕЕ" и "месячный расход" присваиваем значения "0"
                    for j in self.win_pole[1: 12: 2] + self.win_pole[12: 17]:
                        j.setText("0")
        try:
            if int(self.win_pole[1].text()) != 0:
                self.summa_month_ras(12)
                self.summa_month_ras(13)
                self.summa_month_ras(14)
                self.summa_month_ras(16)
        except ValueError:
            self.label_error_COU.show()
            self.label_error_COU.setText('Нет значений для этого периода')

        self.lineEdit_post_P.textEdited[str].connect(lambda: self.summa_month_ras(12))
        self.lineEdit_post_W1.textEdited[str].connect(lambda: self.summa_month_ras(13))
        self.lineEdit_post_W2.textEdited[str].connect(lambda: self.summa_month_ras(14))
        self.lineEdit_post_W3.textEdited[str].connect(lambda: self.summa_month_ras(13))
        self.lineEdit_post_W4.textEdited[str].connect(lambda: self.summa_month_ras(14))
        self.lineEdit_post_G.textEdited[str].connect(lambda: self.summa_month_ras(16))

        self.data = self.create_list_date_counters()  # создает список значений

    def summa_month_ras(self, n):
        try:
            self.label_error_COU.clear()
            self.win_pole[n].setText("0")
            if self.win_pole[n] == self.label_month_ras_P:
                if int(self.win_pole[1].text()) != 0:
                    self.win_pole[n].setText(str(int(self.win_pole[1].text()) - int(self.win_pole[0].text())))
            elif self.win_pole[n] == self.label_month_ras_WC:
                if int(self.win_pole[3].text()) or int(self.win_pole[7].text()) != 0:
                    self.win_pole[n].setText(str((int(self.win_pole[3].text()) - int(self.win_pole[2].text())) +
                                                 (int(self.win_pole[7].text()) - int(self.win_pole[6].text()))))
                    self.win_pole[15].setText(str(int(self.win_pole[13].text()) + int(self.win_pole[14].text())))
            elif self.win_pole[n] == self.label_month_ras_WH:
                if int(self.win_pole[5].text()) or int(self.win_pole[9].text()) != 0:
                    self.win_pole[n].setText(str((int(self.win_pole[5].text()) - int(self.win_pole[4].text())) +
                                                 (int(self.win_pole[9].text()) - int(self.win_pole[8].text()))))
                    self.win_pole[15].setText(str(int(self.win_pole[13].text()) + int(self.win_pole[14].text())))
            elif self.win_pole[n] == self.label_month_ras_G:
                if int(self.win_pole[11].text()) != 0:
                    self.win_pole[n].setText(str(int(self.win_pole[11].text()) - int(self.win_pole[10].text())))
        except ValueError:
            self.label_error_COU.show()
            self.label_error_COU.setText('Должно быть значение!')

    # создает список значений полей для записи в таблицу
    def create_list_date_counters(self):  # список показаний за месяц
        data = [self.comboBox_month_COU.currentIndex() + 1,
                self.comboBox_month_COU.currentText() + " " + self.comboBox_year_COU.currentText()]
        try:
            for field in self.win_pole[0:12]:
                data.append(int(field.text()))
        except ValueError:
            self.label_error_COU.show()
            self.label_error_COU.setText('Нет значений для этого периода')
        return data

    def btn_save_COU(self):
        data = self.create_list_date_counters()  # создает список значений
        table = 'Counters_year_' + self.data[1].split()[1]  # Имя таблицы ("1")
        col_name = 'id'  # Имя колонки
        row_record = self.data[0]  # Имя записи ("1")

        col_id = SQLite3_Data_Base.sqlite3_read_data(self.data_base, table, col_name)[0]

        if row_record in col_id:
            self.label_error_COU.show()
            self.label_error_COU.setText('Такая запись уже существует!')
            self.save_yes_or_not("Counters", self.data_base, data, self.label_error_COU)
        else:
            SQLite3_Data_Base.sqlite3_insert_data(self.data_base, table, data)
            self.read_data_counters()

            # if self.comboBox_month_COU.currentIndex() + 2 != 13:
            #     b = month[self.comboBox_month_COU.currentIndex() + 1]
            #     c = self.comboBox_year_COU.currentText()
            # else:
            #     b = month[self.comboBox_month_COU.currentIndex() - 11]
            #     c = str(int(self.comboBox_year_COU.currentText()) + 1)
            #
            # self.label_month_year_COU.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
            # self.comboBox_month_COU.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
            # self.comboBox_year_COU.setCurrentText(c)  # устанавливает текущий год ("Год")
            #
            # self.read_pokaz_schet()

    def save_yes_or_not(self, name_table, data_base, date, label_error):
        self.save_or_COU = Save_OR()
        self.save_or_COU.save_yes_or_not(name_table, data_base, date, label_error)

    def btn_cancel_COU(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_COU = Counters()
    sys.exit(app.exec_())
