# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon

from res.UIC_CLASS_COMM import UiWinHeaderFooter, label_titul_f, btn_f, lineEdit_pokaz_f, style_scrollbar, scrollArea_f


# окно приложения "ПЛАТЕЖИ"
class UiWinIncomeExpenses(object):
    def setupUi_IAE(self, WinIncomeExpenses):
        self.WinIncomeExpenses = WinIncomeExpenses  # окно
        self.WinIncomeExpenses.setObjectName("Income and Expenses")
        self.WinIncomeExpenses.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinIncomeExpenses.resize(800, 400)
        self.WinIncomeExpenses.setGeometry(QtCore.QRect(560 + 1920 + 395, 300, 800, 400))  #
        self.WinIncomeExpenses.setMinimumSize(QtCore.QSize(800, 400))
        self.WinIncomeExpenses.setFixedWidth(800)
        self.WinIncomeExpenses.activateWindow()
        self.WinIncomeExpenses.setWindowTitle('ДОХОДЫ И РАСХОДЫ')
        self.WinIncomeExpenses.setWindowIcon(QIcon('res/img/Payments-icon.png'))
        self.WinIncomeExpenses.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.ui_head_foot = UiWinHeaderFooter()

        self.centralwidget = QtWidgets.QWidget(self.WinIncomeExpenses)
        self.centralwidget.setStyleSheet(style_scrollbar)
        self.centralwidget.setObjectName("centralwidget")

        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 10, 10, 10)
        self.v_Layout_centralwidget.setSpacing(8)
        self.v_Layout_centralwidget.setObjectName("v_Layout_centralwidget")

        # Frame Header

        (self.frame_ui_header, self.btn_Left_IAE, self.label_month_year_IAE, self.btn_Right_IAE,
         self.label_GL_V_1_IAE, self.label_GL_V_2_IAE) = self.ui_head_foot.ui_win_header(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_header)

        # Frame Group

        self.frame_group = QtWidgets.QFrame(self.centralwidget)
        self.frame_group.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_group.setMaximumSize(QtCore.QSize(780, 300))
        self.frame_group.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_group.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_group.setStyleSheet("background-color: rgb(78, 79, 84); border: 0px solid; padding: 0px;")
        self.frame_group.setObjectName("frame_title")

        self.h_layout_frame_group = QtWidgets.QHBoxLayout(self.frame_group)
        self.h_layout_frame_group.setContentsMargins(0, 0, 0, 0)
        self.h_layout_frame_group.setSpacing(8)
        self.h_layout_frame_group.setObjectName("h_layout_frame_title")

        self.v_Layout_centralwidget.addWidget(self.frame_group)

        # Group Income

        self.income_group = QtWidgets.QGroupBox("Доходы", self.centralwidget)
        self.income_group.setFixedSize(QtCore.QSize(386, 217))
        font = QtGui.QFont("Times", 14, 75)
        self.income_group.setFont(font)
        self.income_group.setStyleSheet("QGroupBox{font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                        "background-color: rgb(100, 100, 100);"
                                        "border: 1px solid rgba(209, 209, 217, 240);};")
        self.income_group.setAlignment(QtCore.Qt.AlignCenter)
        self.income_group.setObjectName("payments_group")

        self.v_layout_inc_group = QtWidgets.QVBoxLayout(self.income_group)
        self.v_layout_inc_group.setContentsMargins(5, 28, 5, 5)
        self.v_layout_inc_group.setSpacing(0)
        self.v_layout_inc_group.setObjectName("v_layout_group_box")

        self.h_layout_frame_group.addWidget(self.income_group)

        self.scrollArea_inc = scrollArea_f(self.income_group, 390, 185)

        self.s_Area_WContents_inc = QtWidgets.QWidget()
        self.s_Area_WContents_inc.setMinimumSize(QtCore.QSize(355, 0))
        self.s_Area_WContents_inc.setMaximumSize(QtCore.QSize(355, 1000))
        self.s_Area_WContents_inc.setObjectName("scrollAreaWidgetContents")

        self.v_layout_scrollArea_inc = QtWidgets.QVBoxLayout(self.s_Area_WContents_inc)
        self.v_layout_scrollArea_inc.setContentsMargins(0, 5, 0, 4)
        self.v_layout_scrollArea_inc.setSpacing(7)
        self.v_layout_scrollArea_inc.setAlignment(QtCore.Qt.AlignTop)
        self.v_layout_scrollArea_inc.setObjectName("v_layout_scrollArea")

        self.scrollArea_inc.setWidget(self.s_Area_WContents_inc)
        self.v_layout_inc_group.addWidget(self.scrollArea_inc)

        # Group Expenses

        self.expenses_group = QtWidgets.QGroupBox("Расходы", self.centralwidget)
        self.expenses_group.setFixedSize(QtCore.QSize(386, 217))
        font = QtGui.QFont("Times", 14, 75)
        self.expenses_group.setFont(font)
        self.expenses_group.setStyleSheet("QGroupBox{font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                          "background-color: rgb(100, 100, 100);"
                                          "border: 1px solid rgba(209, 209, 217, 240);};padding: 0, 0, 0, 0;")
        self.expenses_group.setAlignment(QtCore.Qt.AlignCenter)
        self.expenses_group.setObjectName("payments_group")

        self.v_layout_exp_group = QtWidgets.QVBoxLayout(self.expenses_group)
        self.v_layout_exp_group.setContentsMargins(5, 28, 5, 5)
        self.v_layout_exp_group.setSpacing(0)
        self.v_layout_exp_group.setObjectName("v_layout_group_box")

        self.h_layout_frame_group.addWidget(self.expenses_group)

        self.scrollArea_exp = scrollArea_f(self.expenses_group, 390, 185)

        self.s_Area_WContents_exp = QtWidgets.QWidget()
        self.s_Area_WContents_exp.setMinimumSize(QtCore.QSize(355, 0))  # 250
        self.s_Area_WContents_exp.setMaximumSize(QtCore.QSize(355, 1000))
        self.s_Area_WContents_exp.setObjectName("scrollAreaWidgetContents")

        self.v_layout_scrollArea_exp = QtWidgets.QVBoxLayout(self.s_Area_WContents_exp)
        self.v_layout_scrollArea_exp.setContentsMargins(0, 5, 0, 4)
        self.v_layout_scrollArea_exp.setSpacing(7)
        self.v_layout_scrollArea_exp.setAlignment(QtCore.Qt.AlignTop)
        self.v_layout_scrollArea_exp.setObjectName("v_layout_scrollArea")

        self.scrollArea_exp.setWidget(self.s_Area_WContents_exp)
        self.v_layout_exp_group.addWidget(self.scrollArea_exp)

        # Button Add Payment

        self.btn_add_iae = btn_f("Добавить платеж", self.WinIncomeExpenses, 780, 30, 11)
        self.v_Layout_centralwidget.addWidget(self.btn_add_iae)

        # Frame Result

        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.frame_result = QtWidgets.QFrame(self.centralwidget)
        self.frame_result.setFixedSize(QtCore.QSize(780, 40))
        self.frame_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_result.setStyleSheet("font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                        "background-color: rgb(100, 100, 100); "
                                        "border: 1px solid rgba(209, 209, 217, 240);")
        self.frame_result.setObjectName("frame_result")

        self.h_layout_frame_result = QtWidgets.QHBoxLayout(self.frame_result)
        self.h_layout_frame_result.setContentsMargins(0, 0, 0, 0)
        self.h_layout_frame_result.setSpacing(5)
        self.h_layout_frame_result.setObjectName("h_layout_frame_result")

        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_frame_result.addItem(self.spacerItem)

        self.label_result = label_titul_f("Итого:", self.frame_result, 14)
        self.label_result.setFixedSize(QtCore.QSize(80, 30))
        self.label_result.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.h_layout_frame_result.addWidget(self.label_result)

        self.lineEdit_result = lineEdit_pokaz_f("000.00", self.frame_result, "(255, 255, 216, 200)", grad_1, grad_2)
        self.lineEdit_result.setFixedSize(QtCore.QSize(400, 30))
        self.h_layout_frame_result.addWidget(self.lineEdit_result)

        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_frame_result.addItem(self.spacerItem)

        self.v_Layout_centralwidget.addWidget(self.frame_result)

        # Frame Footer

        (self.frame_ui_footer, self.comboBox_month_IAE, self.comboBox_year_IAE, self.label_error_IAE,
         self.btn_Save_IAE, self.btn_Cancel_IAE) = self.ui_head_foot.ui_win_footer(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_footer)

        QtCore.QMetaObject.connectSlotsByName(self.WinIncomeExpenses)
        # self.WinExpenses.setTabOrder(self.btn_Right_EXP, self.btn_add_exp)
        # self.WinExpenses.setTabOrder(self.btn_add_exp, self.comboBox_month_EXP)
        # self.WinExpenses.setTabOrder(self.comboBox_month_EXP, self.comboBox_year_EXP)
        # self.WinExpenses.setTabOrder(self.comboBox_year_EXP, self.btn_Save_EXP)
        # # self.WinPayment.setTabOrder(self.comboBox_year_EXP, self.label_error_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Save_EXP, self.btn_Cancel_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Cancel_EXP, self.btn_Left_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Left_EXP, self.btn_Right_EXP)
