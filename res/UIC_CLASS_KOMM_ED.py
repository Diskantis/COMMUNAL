# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QCompleter


def btn_f(name, group, xl, yl, font_s):  # кнопки
    btn = QtWidgets.QPushButton(name, group)
    btn.setMinimumSize(QtCore.QSize(xl, yl))
    btn.setMaximumSize(QtCore.QSize(xl, yl))
    font = QtGui.QFont("Times", font_s, 75)
    btn.setFont(font)
    btn.setStyleSheet("color: rgb(255, 255, 216, 200);")
    btn.setAutoDefault(True)
    btn.setObjectName("btn_f")
    return btn


def btn_check_payment(group, xl, yl):
    btn_check = QtWidgets.QPushButton(group)
    btn_check.setMinimumSize(QtCore.QSize(xl, yl))
    btn_check.setMaximumSize(QtCore.QSize(xl, yl))
    btn_check.setStyleSheet("border: 0px solid;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("E:/6_PROGRAMING/1_PROJECT/1_WORK PROJECT/HOME_KOMMUNAL"
                                 "/res/img/icon_checked_n.png"), QIcon.Normal, QIcon.Off)
    icon.addPixmap(QtGui.QPixmap("E:/6_PROGRAMING/1_PROJECT/1_WORK PROJECT/HOME_KOMMUNAL"
                                 "/res/img/icon_checked_o.png"), QIcon.Active, QIcon.On)
    btn_check.setIcon(icon)
    btn_check.setIconSize(QtCore.QSize(30, 30))
    btn_check.setCheckable(True)
    btn_check.setObjectName("btn_check")
    return btn_check


def label_f(name, group, xl, yl, font_s):  # заголовки
    label = QtWidgets.QLabel(name, group)
    label.setMinimumSize(QtCore.QSize(xl, yl))
    font = QtGui.QFont("Times", font_s, QtGui.QFont.Bold)
    label.setFont(font)
    label.setStyleSheet("border-radius: 2px; color: rgb(255,255,216,200); border: 1px solid rgba(50, 50, 50, 240); "
                        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                        "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                        "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setObjectName("label_month_year")
    return label


def label_titul_f(name, group, font_s=None):
    label_titul = QtWidgets.QLabel(name, group)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    label_titul.setSizePolicy(sizePolicy)
    label_titul.setMinimumSize(QtCore.QSize(100, 25))
    label_titul.setMaximumSize(QtCore.QSize(780, 25))
    if font_s is not None:
        font = QtGui.QFont("Times", font_s, 75)
    else:
        font = QtGui.QFont("Times", 10, 75)
    label_titul.setFont(font)
    label_titul.setStyleSheet("color: rgb(209, 209, 217); padding: 0px; border: 0px solid rgba(50, 50, 50, 240);")
    label_titul.setAlignment(QtCore.Qt.AlignCenter)
    label_titul.setObjectName("label_pred")
    return label_titul


def lineEdit_pokaz_f(name, group, color, grad_1, grad_2):  # значения счетчиков
    lineEdit_pokaz = QtWidgets.QLineEdit(name, group)
    lineEdit_pokaz.setMinimumSize(QtCore.QSize(80, 30))
    lineEdit_pokaz.setMaximumSize(QtCore.QSize(780, 30))
    font = QtGui.QFont("Times", 12, 75)
    lineEdit_pokaz.setFont(font)
    lineEdit_pokaz.setStyleSheet(
        "border-radius: 2px; color: rgb" + color + "; border: 1px solid rgba(50, 50, 50, 240); "
        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba" + grad_1 + ", stop:0.98 rgba" + grad_2 + ","
        "stop:1 rgba(125, 126, 131, 255));")
    lineEdit_pokaz.setObjectName("lineEdit_post_pokaz")
    lineEdit_pokaz.setAlignment(QtCore.Qt.AlignCenter)
    lineEdit_pokaz.setContextMenuPolicy(Qt.CustomContextMenu)
    lineEdit_pokaz.setReadOnly(True)
    return lineEdit_pokaz


def comboBox_f(group, xl, yl):  # выбор месяца или года
    comboBox = QtWidgets.QComboBox(group)
    comboBox.setMinimumSize(QtCore.QSize(xl, yl))
    comboBox.setMaximumSize(QtCore.QSize(xl, yl))
    font = QtGui.QFont("Times", 11, 75)
    comboBox.setFont(font)
    comboBox.setMaxVisibleItems(5)
    comboBox.setStyleSheet("QComboBox {combobox-popup: 0; font-size: 50%; font-weight: 700; "
                           "color: rgb(255, 255, 216, 200);}")
    comboBox.setObjectName("comboBox")
    return comboBox


class UiWinHeaderFooter(object):
    def ui_win_header(self, Win_app):
        self.frame_ui_header = QtWidgets.QFrame(Win_app)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.frame_ui_header.setSizePolicy(sizePolicy)
        self.frame_ui_header.setMinimumSize(QtCore.QSize(780, 30))
        self.frame_ui_header.setMaximumSize(QtCore.QSize(780, 30))
        self.frame_ui_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ui_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ui_header.setObjectName("frame_ui_head")

        self.h_Layout_header = QtWidgets.QHBoxLayout(self.frame_ui_header)
        self.h_Layout_header.setContentsMargins(0, 0, 0, 0)
        self.h_Layout_header.setObjectName("h_Layout_head")

        self.btn_Left = btn_f("<", self.frame_ui_header, 30, 30, 10)
        self.btn_Left.setShortcut(Qt.Key_Left)
        self.h_Layout_header.addWidget(self.btn_Left)

        self.label_month_year = label_f("TextLabel", self.frame_ui_header, 700, 30, 14)
        self.h_Layout_header.addWidget(self.label_month_year)

        self.btn_Right = btn_f(">", self.frame_ui_header, 30, 30, 10)
        self.btn_Right.setShortcut(Qt.Key_Right)
        self.h_Layout_header.addWidget(self.btn_Right)

        self.label_GL_V_1 = label_f("", self.frame_ui_header, 36, 36, 14)
        self.label_GL_V_1.setGeometry(QtCore.QRect(34, -3, 36, 36))
        self.label_GL_V_1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.label_GL_V_1.setScaledContents(True)
        self.label_GL_V_1.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0px solid;")

        self.label_GL_V_2 = label_f("", self.frame_ui_header, 36, 36, 14)
        self.label_GL_V_2.setGeometry(QtCore.QRect(710, -3, 36, 36))
        self.label_GL_V_2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.label_GL_V_2.setScaledContents(True)
        self.label_GL_V_2.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0px solid;")

        return (self.frame_ui_header, self.btn_Left, self.label_month_year, self.btn_Right,
                self.label_GL_V_1, self.label_GL_V_2)

    def ui_win_footer(self, Win_app):
        self.frame_ui_footer = QtWidgets.QFrame(Win_app)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.frame_ui_footer.setSizePolicy(sizePolicy)
        self.frame_ui_footer.setMinimumSize(QtCore.QSize(780, 30))
        self.frame_ui_footer.setMaximumSize(QtCore.QSize(780, 30))
        self.frame_ui_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ui_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ui_footer.setObjectName("frame_ui_footer")

        self.h_Layout_footer = QtWidgets.QHBoxLayout(self.frame_ui_footer)
        self.h_Layout_footer.setContentsMargins(0, 0, 0, 0)
        self.h_Layout_footer.setSpacing(10)
        self.h_Layout_footer.setObjectName("h_Layout_footer")

        self.comboBox_month = comboBox_f(self.frame_ui_footer, 130, 30)
        self.h_Layout_footer.addWidget(self.comboBox_month)

        self.comboBox_year = comboBox_f(self.frame_ui_footer, 90, 30)
        self.h_Layout_footer.addWidget(self.comboBox_year)

        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_Layout_footer.addItem(self.spacerItem)

        self.label_error = label_f("", self.frame_ui_footer, 300, 30, 12)
        self.label_error.setStyleSheet("font-weight: 700; color: rgba(255, 255, 0); padding: .4em 1em;")
        self.label_error.hide()
        self.h_Layout_footer.addWidget(self.label_error)

        self.btn_Save = btn_f("Сохранить", self.frame_ui_footer, 110, 30, 10)
        self.h_Layout_footer.addWidget(self.btn_Save)

        self.btn_Cancel = btn_f("Отмена", self.frame_ui_footer, 110, 30, 10)
        self.h_Layout_footer.addWidget(self.btn_Cancel)

        return (self.frame_ui_footer, self.comboBox_month, self.comboBox_year, self.label_error,
                self.btn_Save, self.btn_Cancel)


class UiWinGrouper(object):
    def __init__(self, name, Win_app):
        self.group_box = QtWidgets.QGroupBox(name, Win_app)
        self.group_box.setMinimumSize(QtCore.QSize(230, 300))
        self.group_box.setMaximumSize(QtCore.QSize(780, 300))
        font = QtGui.QFont("Times", 14, 75)
        self.group_box.setFont(font)
        self.group_box.setStyleSheet("font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                     "background-color: rgb(100, 100, 100); "
                                     "border: 1px solid rgba(209, 209, 217, 240);")
        self.group_box.setAlignment(QtCore.Qt.AlignCenter)
        self.group_box.setObjectName("grPowerBox")

        self.v_layout_group_box = QtWidgets.QVBoxLayout(self.group_box)
        self.v_layout_group_box.setContentsMargins(0, 0, 0, 0)
        self.v_layout_group_box.setSpacing(0)
        self.v_layout_group_box.setObjectName("v_layout_group_box")

        self.spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_layout_group_box.addItem(self.spacerItem)

        self.fr_line_ed = QtWidgets.QFrame(self.group_box)
        self.fr_line_ed.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_line_ed.setMaximumSize(QtCore.QSize(780, 300))
        self.fr_line_ed.setStyleSheet("QFrame {border: 0px solid; padding: 0px;};")
        self.fr_line_ed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_line_ed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_line_ed.setLineWidth(0)
        self.fr_line_ed.setObjectName("frame_line_ed")

        self.g_layout_fr_line_ed = QtWidgets.QGridLayout(self.fr_line_ed)
        self.g_layout_fr_line_ed.setContentsMargins(8, 0, 8, 8)
        self.g_layout_fr_line_ed.setSpacing(5)
        self.g_layout_fr_line_ed.setObjectName("g_layout_fr_line_ed")

        self.v_layout_group_box.addWidget(self.fr_line_ed)

        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_layout_group_box.addItem(self.spacerItem)

        self.fr_month_ras = QtWidgets.QFrame(self.group_box)
        self.fr_month_ras.setMinimumSize(QtCore.QSize(210, 0))
        self.fr_month_ras.setMaximumSize(QtCore.QSize(780, 300))
        self.fr_month_ras.setStyleSheet("QFrame {border: 0px solid; padding: 0px;}")
        self.fr_month_ras.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_month_ras.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_month_ras.setLineWidth(0)
        self.fr_month_ras.setObjectName("fr_label_month_ras")

        self.h_layout_fr_month_ras = QtWidgets.QHBoxLayout(self.fr_month_ras)
        self.h_layout_fr_month_ras.setContentsMargins(0, 0, 0, 0)
        self.h_layout_fr_month_ras.setSpacing(5)
        self.h_layout_fr_month_ras.setObjectName("h_Layout_fr_label_month_ras")

        self.g_layout_fr_line_ed.addWidget(self.fr_month_ras, 9, 0, 1, 2)


class Ui_Widget_Payment(object):
    def setupUi(self, Widget_Pay):
        # слой вертикального выравнивания виджета
        self.h_Layout_widget_Team = QtWidgets.QHBoxLayout(Widget_Pay)
        self.h_Layout_widget_Team.setContentsMargins(8, 0, 8, 0)
        self.h_Layout_widget_Team.setSpacing(8)
        self.h_Layout_widget_Team.setObjectName("v_Layout_widget_Team")

        color = "(209, 209, 217)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.btn_check = btn_check_payment(Widget_Pay, 30, 30)
        self.h_Layout_widget_Team.addWidget(self.btn_check)

        self.label_payment = label_titul_f("", Widget_Pay, 12)
        self.label_payment.setMinimumSize(QtCore.QSize(200, 25))
        self.label_payment.setStyleSheet("border: 0px solid rgba(209, 209, 217, 240); padding: 0;")
        self.label_payment.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.h_Layout_widget_Team.addWidget(self.label_payment)

        self.l_edit_sum = lineEdit_pokaz_f("", Widget_Pay, color, grad_1, grad_2)
        self.h_Layout_widget_Team.addWidget(self.l_edit_sum)

        self.l_edit_quantity = lineEdit_pokaz_f("", Widget_Pay, color, grad_1, grad_2)
        self.h_Layout_widget_Team.addWidget(self.l_edit_quantity)

        self.l_edit_tariff = lineEdit_pokaz_f("", Widget_Pay, color, grad_2, grad_1)
        self.h_Layout_widget_Team.addWidget(self.l_edit_tariff)


class UiWinAdd(QtWidgets.QDialog):  # окно создания ДОЛНИТЕЛЬНЫХ ПЛАТЕЖЕЙ
    def __init__(self):
        super().__init__()

    def name_platega(self):
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Добавление платежа")
        self.resize(300, 120)
        self.setStyleSheet("background-color: rgb(78, 79, 84);")
        self.setObjectName("Form")

        self.label = label_f("Имя платежа", self, 270, 30, 12)
        self.label.setGeometry(QtCore.QRect(10, 5, 270, 30))
        self.label.setStyleSheet("font-weight: 700; color: rgb(209, 209, 217); padding: .1em; border: 1px;")

        self.lineEdit = lineEdit_pokaz_f("", self, "(209, 209, 217)", "(108, 109, 114, 255)", "(91, 92, 96, 255)")

        strList = ['Квартира', 'Телефон', 'Интернет', 'Гимназия пит.', 'Гимназия кру.', 'R-ED.', 'Зарплата МИША (ОНТ)',
                   'Зарплата ОЛЯ (ОНТ)']

        completer = QCompleter(strList, self.lineEdit)
        self.lineEdit.setCompleter(completer)
        font = QtGui.QFont()
        font.setPointSize(11)
        completer.popup().setFont(font)
        completer.popup().setStyleSheet("font-weight: 600; color:rgb(209, 209, 217); background-color:rgb(78, 79, 84);")

        self.btn_OK = btn_f("OK", self, 110, 30, 10)
        self.btn_OK.setGeometry(QtCore.QRect(30, 80, 110, 30))

        self.btn_Cancel = btn_f("Отмена", self, 110, 30, 10)
        self.btn_Cancel.setGeometry(QtCore.QRect(150, 80, 110, 30))

        self.show()

        return strList

# def btn_check_plateg(name, group, x, y, xl, yl):
#     btn_check = QtWidgets.QPushButton(name, group)
#     btn_check.setGeometry(QtCore.QRect(x, y, xl, yl))
#     btn_check.setStyleSheet("border: 0px solid;")
#     icon = QtGui.QIcon()
#     icon.addPixmap(QtGui.QPixmap("./Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#     icon.addPixmap(QtGui.QPixmap("./Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
#     btn_check.setIcon(icon)
#     btn_check.setIconSize(QtCore.QSize(30, 30))
#     btn_check.setCheckable(True)
#     btn_check.setObjectName("btn_check")
#     return btn_check
#
# def radio_btn(name, group, x, y, xl, yl):
#     rad_btn = QtWidgets.QRadioButton(name, group)
#     rad_btn.setGeometry(QtCore.QRect(x, y, xl, yl))
#     font = QtGui.QFont()
#     font.setPointSize(12)
#     rad_btn.setFont(font)
#     rad_btn.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 1px;")
#     rad_btn.setObjectName("radioButton")
#     return rad_btn
#
#
# class UiWinAdd_1(QtWidgets.QDialog):  # метод создания ДОЛНИТЕЛЬНЫХ ПЛАТЕЖЕЙ
#     def __init__(self):
#         super().__init__()
#
#     def name_plateg(self):
#         self.setObjectName("Form")
#         self.setWindowModality(QtCore.Qt.ApplicationModal)
#         self.resize(290, 120)
#         self.setStyleSheet("background-color: rgb(78, 79, 84);")
#         self.setWindowTitle("Добавление платежа")
#
#         self.label = label_plateg("Имя платежа", self, 10, 5, 270, 30)
#         self.label.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 1px;")
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#
#         self.lineEdit = QtWidgets.QLineEdit(self)
#         self.lineEdit.setGeometry(QtCore.QRect(10, 40, 270, 30))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setWeight(75)
#         self.lineEdit.setFont(font)
#         self.lineEdit.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
#                                     "border: 1px solid rgba(50, 50, 50, 240); \n "
#                                     "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
#                                     "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
#                                     "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
#         self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
#         self.lineEdit.setFocus()
#         self.lineEdit.setObjectName("lineEdit")
#
#         strList = ['Квартира', 'Телефон', 'Интернет', 'Детский сад', 'Космос ТВ', 'Зарплата МИША (ОНТ)',
#                    'Зарплата МИША (БелМУЗ)', 'Зарплата ОЛЯ (ОНТ)']
#         completer = QCompleter(strList, self.lineEdit)
#         self.lineEdit.setCompleter(completer)
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         completer.popup().setFont(font)
#         completer.popup().setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
#                                         "background-color: rgb(78, 79, 84); ")
#
#         self.btn_OK = btn_f("OK", self, 30, 80, 110, 30)
#         self.btn_OK.setAutoDefault(True)
#         self.btn_OK.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
#
#         self.btn_Cancel = btn_f("Отмена", self, 150, 80, 110, 30)
#         self.btn_Cancel.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
#
#         self.show()
#
#         return strList
#
#     def radio_btn(self):
#         self.setObjectName("Form")
#         self.setWindowModality(QtCore.Qt.ApplicationModal)
#         self.resize(290, 120)
#         self.setStyleSheet("background-color: rgb(78, 79, 84);")
#         self.setWindowTitle("Выбор раздела")
#
#         self.rad_btn_1 = radio_btn("Доходы", self, 35, 25, 110, 30)
#         self.rad_btn_2 = radio_btn("Расходы", self, 155, 25, 110, 30)
#
#         self.btn_OK = btn_f("OK", self, 30, 80, 110, 30)
#         self.btn_OK.setAutoDefault(True)
#         self.btn_OK.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
#
#         self.btn_Cancel = btn_f("Отмена", self, 150, 80, 110, 30)
#         self.btn_Cancel.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
#
#         self.show()


def label_plateg(label_name, group, x, y, xl, yl):
    label_plat = QtWidgets.QLabel(label_name, group)
    label_plat.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(87)
    label_plat.setFont(font)
    label_plat.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n border: 0px solid;")
    label_plat.setObjectName("label_plat")
    return label_plat


def line_edit_pokaz(group, x, y, xl, yl, color, grad_1, grad_2):
    lineEdit_pokaz = QtWidgets.QLineEdit(group)
    lineEdit_pokaz.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setWeight(75)
    lineEdit_pokaz.setFont(font)
    lineEdit_pokaz.setStyleSheet("border-radius: 4px; \n color: rgb" + color
                                 + "; \n border: 1px solid rgba(50, 50, 50, 240); \n "
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba" + grad_1 + ", stop:0.99 rgba"
                                 + grad_2 + ", stop:1 rgba(125, 126, 131, 255));")
    lineEdit_pokaz.setAlignment(QtCore.Qt.AlignCenter)
    lineEdit_pokaz.setReadOnly(True)
    lineEdit_pokaz.setObjectName("lineEdit_pokaz")
    return lineEdit_pokaz


def btn_check_plateg(name, group, x, y, xl, yl):
    btn_check = QtWidgets.QPushButton(name, group)
    btn_check.setGeometry(QtCore.QRect(x, y, xl, yl))
    btn_check.setStyleSheet("border: 0px solid;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap("./Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
    btn_check.setIcon(icon)
    btn_check.setIconSize(QtCore.QSize(30, 30))
    btn_check.setCheckable(True)
    btn_check.setObjectName("btn_check")
    return btn_check


class NewPlateg(QtWidgets.QWidget):
    def __init__(self, name, summ):
        super(NewPlateg, self).__init__()

        self.label_Plat = label_plateg(name, self, 40, 1, 130, 30)
        self.btn_check_Plat = btn_check_plateg(self, 0, 1, 30, 30)

        color = "(209, 209, 217)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Plat = line_edit_pokaz(self, 180, 1, 190, 30, color, grad_2, grad_1)
        self.lineEdit_sum_Plat.setText(summ + " руб")
        self.lineEdit_sum_Plat.setReadOnly(False)

        self.btn_del_Plat = btn_check_plateg(self, 720, 2, 30, 30)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resource/img/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_Plat.setIcon(icon)
