# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from res.DLL_CLASS_COMM import Widget_Payment
from res.UIC_CLASS_COMM import UiWinHeaderFooter, label_titul_f, lineEdit_pokaz_f, style_scrollbar, btn_check_payment


# окно приложения "КОМУНАЛЬНЫЕ ПЛАТЕЖИ"
class UiWinPayment(object):
    def setupUi_PAY(self, WinPayment):
        self.WinPayment = WinPayment  # окно
        self.WinPayment.setObjectName("CommunalPayment")
        self.WinPayment.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPayment.resize(800, 400)
        self.WinPayment.setGeometry(QtCore.QRect(560 + 1920-415, 300, 800, 400))
        self.WinPayment.setFixedSize(QtCore.QSize(800, 400))
        self.WinPayment.activateWindow()
        self.WinPayment.setWindowTitle('КОМУНАЛЬНЫЕ ПЛАТЕЖИ')
        self.WinPayment.setWindowIcon(QIcon('res/img/Payments-icon.png'))
        self.WinPayment.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.ui_head_foot = UiWinHeaderFooter()

        self.centralwidget = QtWidgets.QWidget(self.WinPayment)
        self.centralwidget.setStyleSheet(style_scrollbar)
        self.centralwidget.setObjectName("centralwidget")

        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 10, 10, 10)
        self.v_Layout_centralwidget.setSpacing(8)
        self.v_Layout_centralwidget.setObjectName("v_Layout_centralwidget")

        # Frame Header

        (self.frame_ui_header, self.btn_Left_PAY, self.label_month_year_PAY, self.btn_Right_PAY,
         self.label_GL_V_1_PAY, self.label_GL_V_2_PAY) = self.ui_head_foot.ui_win_header(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_header)

        # Group Payment

        self.payments_group = QtWidgets.QGroupBox("Коммунальные платежи", self.centralwidget)
        self.payments_group.setFixedSize(QtCore.QSize(780, 255))
        font = QtGui.QFont("Times", 14, 75)
        self.payments_group.setFont(font)
        self.payments_group.setStyleSheet("QGroupBox{font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                          "background-color: rgb(100, 100, 100);"
                                          "border: 1px solid rgba(209, 209, 217, 240);};")
        self.payments_group.setAlignment(QtCore.Qt.AlignCenter)
        self.payments_group.setObjectName("payments_group")

        self.v_layout_pay_group = QtWidgets.QVBoxLayout(self.payments_group)
        self.v_layout_pay_group.setContentsMargins(6, 25, 8, 0)
        self.v_layout_pay_group.setSpacing(5)
        self.v_layout_pay_group.setAlignment(Qt.AlignTop)
        self.v_layout_pay_group.setObjectName("v_layout_group_box")

        self.v_Layout_centralwidget.addWidget(self.payments_group)

        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title.setMaximumSize(QtCore.QSize(780, 30))
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title.setStyleSheet("background-color: rgb(100, 100, 100); border: 0px solid; padding: 0px;")
        self.frame_title.setObjectName("frame_title")

        self.h_layout_frame_title = QtWidgets.QHBoxLayout(self.frame_title)
        self.h_layout_frame_title.setContentsMargins(0, 0, 0, 0)
        self.h_layout_frame_title.setSpacing(8)
        self.h_layout_frame_title.setObjectName("h_layout_frame_title")

        self.v_layout_pay_group.addWidget(self.frame_title)

        self.label_dummy = label_titul_f("", self.frame_title)
        self.label_dummy.setFixedSize(QtCore.QSize(185, 18))
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

        self.btn_check_all = btn_check_payment(self.payments_group, 186, 28)
        self.btn_check_all.move(QtCore.QPoint(8, 8))
        self.btn_check_all.setStyleSheet("color: rgb(209, 209, 217); background-color: rgba(255, 255, 255, 0); "
                                         "border: 0px solid rgba(50, 50, 50, 240); padding: 0px; text-align: left;")

        self.list_payments = []
        self.list_payments_name = []

        self.pay_power = Widget_Payment("Электричество", "(0, 160, 0)")
        self.list_payments.append(self.pay_power.btn_check)
        self.list_payments_name.append(self.pay_power.btn_check.text())
        self.pay_power.commpay()
        self.v_layout_pay_group.addWidget(self.pay_power)

        self.pay_water = Widget_Payment("Вода", "(0, 170, 255)")
        self.list_payments.append(self.pay_water.btn_check)
        self.list_payments_name.append(self.pay_water.btn_check.text())
        self.pay_water.commpay()
        self.v_layout_pay_group.addWidget(self.pay_water)

        self.pay_gaz = Widget_Payment("Газ", "(150, 0, 150)")
        self.list_payments.append(self.pay_gaz.btn_check)
        self.list_payments_name.append(self.pay_gaz.btn_check.text())
        self.pay_gaz.commpay()
        self.v_layout_pay_group.addWidget(self.pay_gaz)

        self.separator = QtWidgets.QFrame()
        self.separator.setMinimumSize(QtCore.QSize(750, 2))
        self.separator.setMaximumSize(QtCore.QSize(780, 2))
        self.separator.setAutoFillBackground(False)
        self.separator.setContentsMargins(0, 0, 0, 0)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setLineWidth(1)
        self.separator.setMidLineWidth(1)
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setObjectName("separator")
        self.v_layout_pay_group.addWidget(self.separator)

        self.pay_apartment = Widget_Payment("Квартира", "(209, 209, 217)")
        self.list_payments.append(self.pay_apartment.btn_check)
        self.list_payments_name.append(self.pay_apartment.btn_check.text())
        self.pay_apartment.commpay()
        self.pay_apartment.line_edit_sum.setStyleSheet(
            "border-radius: 2px; color: rgb(209, 209, 217); border: 1px solid rgba(50, 50, 50, 240); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
            "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(108, 109, 114, 255), stop:0.98 rgba(91, 92, 96, 255),"
            "stop:1 rgba(125, 126, 131, 255));")
        self.pay_apartment.line_edit_sum.setReadOnly(False)
        self.pay_apartment.line_edit_balance_sum = self.pay_apartment.line_edit_quantity
        self.pay_apartment.line_edit_balance_sum.setStyleSheet(
            "border-radius: 2px; color: rgb(255, 163, 24); border: 1px solid rgba(50, 50, 50, 240); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
            "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), stop:0.98 rgba(108, 109, 114, 255),"
            "stop:1 rgba(125, 126, 131, 255));")
        self.pay_apartment.line_edit_minus_water = self.pay_apartment.line_edit_tariff
        self.pay_apartment.line_edit_minus_water.setStyleSheet(
            "border-radius: 2px; color: rgb(0, 170, 255); border: 1px solid rgba(50, 50, 50, 240); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
            "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), stop:0.98 rgba(108, 109, 114, 255),"
            "stop:1 rgba(125, 126, 131, 255));")
        self.pay_apartment.line_edit_minus_water.setReadOnly(True)

        self.v_layout_pay_group.addWidget(self.pay_apartment)

        self.pay_internet = Widget_Payment("Интернет", "(209, 209, 217)")
        self.list_payments.append(self.pay_internet.btn_check)
        self.list_payments_name.append(self.pay_internet.btn_check.text())
        self.v_layout_pay_group.addWidget(self.pay_internet)

        self.pay_phone = Widget_Payment("Телефон", "(209, 209, 217)")
        self.list_payments.append(self.pay_phone.btn_check)
        self.list_payments_name.append(self.pay_phone.btn_check.text())
        self.v_layout_pay_group.addWidget(self.pay_phone)

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

        (self.frame_ui_footer, self.comboBox_month_PAY, self.comboBox_year_PAY, self.label_error_PAY,
         self.btn_Save_PAY, self.btn_Cancel_PAY) = self.ui_head_foot.ui_win_footer(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_footer)

        QtCore.QMetaObject.connectSlotsByName(self.WinPayment)
        self.WinPayment.setTabOrder(self.btn_Right_PAY, self.pay_apartment.line_edit_sum)
        self.WinPayment.setTabOrder(self.pay_apartment.line_edit_sum, self.pay_internet.line_edit_sum)
        self.WinPayment.setTabOrder(self.pay_internet.line_edit_sum, self.pay_phone.line_edit_sum)
        self.WinPayment.setTabOrder(self.pay_phone.line_edit_sum, self.btn_Save_PAY)
        self.WinPayment.setTabOrder(self.btn_Save_PAY, self.btn_Cancel_PAY)
        self.WinPayment.setTabOrder(self.btn_Cancel_PAY, self.comboBox_month_PAY)
        self.WinPayment.setTabOrder(self.comboBox_month_PAY, self.comboBox_year_PAY)
        self.WinPayment.setTabOrder(self.comboBox_year_PAY, self.pay_power.line_edit_tariff)
        self.WinPayment.setTabOrder(self.pay_power.line_edit_tariff, self.pay_water.line_edit_tariff)
        self.WinPayment.setTabOrder(self.pay_water.line_edit_tariff, self.pay_gaz.line_edit_tariff)
        self.WinPayment.setTabOrder(self.pay_gaz.line_edit_tariff, self.btn_Left_PAY)
        self.WinPayment.setTabOrder(self.btn_Left_PAY, self.btn_Right_PAY)
