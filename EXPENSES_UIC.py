# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon

from res.UIC_CLASS_COMM import UiWinHeaderFooter, label_titul_f, btn_f, lineEdit_pokaz_f, style_scrollbar


# окно приложения "ПЛАТЕЖИ"
class UiWinExpenses(object):
    def setupUi_EXP(self, WinExpenses):
        self.WinExpenses = WinExpenses  # окно
        self.WinExpenses.setObjectName("Income and Expenses")
        self.WinExpenses.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinExpenses.resize(800, 400)
        self.WinExpenses.setGeometry(QtCore.QRect(560 + 1920+400, 300, 800, 400))
        self.WinExpenses.setMinimumSize(QtCore.QSize(800, 400))
        self.WinExpenses.setFixedWidth(800)
        self.WinExpenses.setWindowTitle('ДОХОДЫ И РАСХОДЫ')
        self.WinExpenses.setWindowIcon(QIcon('res/img/Payments-icon.png'))
        self.WinExpenses.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.ui_head_foot = UiWinHeaderFooter()

        self.centralwidget = QtWidgets.QWidget(self.WinExpenses)
        self.centralwidget.setStyleSheet(style_scrollbar)
        self.centralwidget.setObjectName("centralwidget")

        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 10, 10, 10)
        self.v_Layout_centralwidget.setSpacing(8)
        self.v_Layout_centralwidget.setObjectName("v_Layout_centralwidget")

        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        # Frame Header

        (self.frame_ui_header, self.btn_Left_EXP, self.label_month_year_EXP, self.btn_Right_EXP,
         self.label_GL_V_1_EXP, self.label_GL_V_2_EXP) = self.ui_head_foot.ui_win_header(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_header)

        # Group Expenses

        self.expenses_group = QtWidgets.QGroupBox("Доходы и Расходы", self.centralwidget)
        self.expenses_group.setFixedSize(QtCore.QSize(780, 217))
        font = QtGui.QFont("Times", 14, 75)
        self.expenses_group.setFont(font)
        self.expenses_group.setStyleSheet("QGroupBox{font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                          "background-color: rgb(100, 100, 100);"
                                          "border: 1px solid rgba(209, 209, 217, 240);};")
        self.expenses_group.setAlignment(QtCore.Qt.AlignCenter)
        self.expenses_group.setObjectName("payments_group")

        self.v_layout_exp_group = QtWidgets.QVBoxLayout(self.expenses_group)
        self.v_layout_exp_group.setContentsMargins(3, 25, 8, 0)
        self.v_layout_exp_group.setSpacing(0)
        self.v_layout_exp_group.setObjectName("v_layout_group_box")

        self.v_Layout_centralwidget.addWidget(self.expenses_group)

        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title.setMaximumSize(QtCore.QSize(740, 30))
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title.setStyleSheet("background-color: rgb(100, 100, 100); border: 0px solid; padding: 0px;")
        self.frame_title.setObjectName("frame_title")

        self.h_layout_frame_title = QtWidgets.QHBoxLayout(self.frame_title)
        self.h_layout_frame_title.setContentsMargins(8, 0, 0, 0)
        self.h_layout_frame_title.setSpacing(8)
        self.h_layout_frame_title.setObjectName("h_layout_frame_title")

        self.v_layout_exp_group.addWidget(self.frame_title)

        self.label_dummy = label_titul_f("", self.frame_title)
        self.label_dummy.setFixedSize(QtCore.QSize(238, 18))
        self.h_layout_frame_title.addWidget(self.label_dummy)

        self.label_sum = label_titul_f("сумма", self.frame_title)
        self.label_sum.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_sum)

        self.label_quantity = label_titul_f("количество", self.frame_title)
        self.label_quantity.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_quantity)

        self.label_tariff = label_titul_f("тариф", self.frame_title)
        self.label_tariff.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_tariff)

        self.scrollArea = QtWidgets.QScrollArea(self.expenses_group)
        self.scrollArea.setMaximumSize(QtCore.QSize(780, 170))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setStyleSheet("background-color: rgb(100, 100, 100); padding: 0, 8, 0, 0;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(752, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(752, 500))
        # self.scrollAreaWidgetContents.setStyleSheet("border: 1px solid rgba(209, 209, 217, 240);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.v_layout_scrollArea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.v_layout_scrollArea.setContentsMargins(0, 4, 0, 4)
        self.v_layout_scrollArea.setSpacing(5)
        self.v_layout_scrollArea.setObjectName("v_layout_scrollArea")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.v_layout_exp_group.addWidget(self.scrollArea)

        self.spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_layout_exp_group.addItem(self.spacerItem)

        # Button Add Payment

        self.btn_add_exp = btn_f("Добавить платеж", self.WinExpenses, 780, 30, 11)
        self.v_Layout_centralwidget.addWidget(self.btn_add_exp)

        # Frame Result

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

        (self.frame_ui_footer, self.comboBox_month_EXP, self.comboBox_year_EXP, self.label_error_EXP,
         self.btn_Save_EXP, self.btn_Cancel_EXP) = self.ui_head_foot.ui_win_footer(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_footer)

        QtCore.QMetaObject.connectSlotsByName(self.WinExpenses)
        # self.WinExpenses.setTabOrder(self.btn_Right_EXP, self.btn_add_exp)
        # self.WinExpenses.setTabOrder(self.btn_add_exp, self.comboBox_month_EXP)
        # self.WinExpenses.setTabOrder(self.comboBox_month_EXP, self.comboBox_year_EXP)
        # self.WinExpenses.setTabOrder(self.comboBox_year_EXP, self.btn_Save_EXP)
        # # self.WinPayment.setTabOrder(self.comboBox_year_EXP, self.label_error_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Save_EXP, self.btn_Cancel_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Cancel_EXP, self.btn_Left_EXP)
        # self.WinExpenses.setTabOrder(self.btn_Left_EXP, self.btn_Right_EXP)
