# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPalette

from res.UIC_CLASS_KOMM_ED import UiWinHeaderFooter, label_titul_f, btn_f, lineEdit_pokaz_f


# окно приложения "ПЛАТЕЖИ"
class UiWinPayment(object):
    def setupUi_CP(self, WinPayment):
        self.WinPayment = WinPayment  # окно
        self.WinPayment.setObjectName("CommunalPayment")
        self.WinPayment.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPayment.resize(800, 400)  # 365
        self.WinPayment.setGeometry(QtCore.QRect(560 + 1960, 200 + 395, 800, 400))
        self.WinPayment.setMinimumSize(QtCore.QSize(800, 400))
        self.WinPayment.setFixedWidth(800)
        self.WinPayment.setWindowTitle('КОМУНАЛЬНЫЕ ПЛАТЕЖИ')
        self.WinPayment.setWindowIcon(QIcon('res/img/payment-icon.png'))
        self.WinPayment.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.ui_head_foot = UiWinHeaderFooter()

        self.centralwidget = QtWidgets.QWidget(self.WinPayment)
        self.centralwidget.setObjectName("centralwidget")

        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 10, 10, 10)
        self.v_Layout_centralwidget.setSpacing(10)
        self.v_Layout_centralwidget.setObjectName("v_Layout_centralwidget")

        # color = "(209, 209, 217)"

        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        # Frame Header

        (self.frame_ui_header, self.btn_Left_CP, self.label_month_year_CP, self.btn_Right_CP,
         self.label_GL_V_1_CP, self.label_GL_V_2_CP) = self.ui_head_foot.ui_win_header(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_header)

        # Group Payment

        self.payments_group = QtWidgets.QGroupBox("Коммунальные платежи", self.centralwidget)
        # self.payments_group.setMinimumSize(QtCore.QSize(780, 30))
        # self.payments_group.setMaximumSize(QtCore.QSize(780, 205))
        self.payments_group.setFixedSize(QtCore.QSize(780, 195))
        font = QtGui.QFont("Times", 14, 75)
        self.payments_group.setFont(font)
        self.payments_group.setStyleSheet("font-weight: 700; color: rgb(209, 209, 217); border-radius: 5px; "
                                          "background-color: rgb(100, 100, 100); "
                                          "border: 1px solid rgba(209, 209, 217, 240);")
        self.payments_group.setAlignment(QtCore.Qt.AlignCenter)
        self.payments_group.setObjectName("payments_group")

        self.v_layout_pay_group = QtWidgets.QVBoxLayout(self.payments_group)
        self.v_layout_pay_group.setContentsMargins(0, 25, 0, 0)
        self.v_layout_pay_group.setSpacing(5)
        self.v_layout_pay_group.setObjectName("v_layout_group_box")

        self.v_Layout_centralwidget.addWidget(self.payments_group)

        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_title.setMaximumSize(QtCore.QSize(750, 30))
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title.setStyleSheet("QFrame {border: 0px solid; padding: 0px;};")
        self.frame_title.setObjectName("frame_title")

        self.h_layout_frame_title = QtWidgets.QHBoxLayout(self.frame_title)
        self.h_layout_frame_title.setContentsMargins(8, 0, 0, 0)
        self.h_layout_frame_title.setSpacing(8)
        self.h_layout_frame_title.setObjectName("h_layout_frame_title")

        self.v_layout_pay_group.addWidget(self.frame_title)

        self.label_pust = label_titul_f("", self.frame_title)
        self.label_pust.setFixedSize(QtCore.QSize(238, 18))
        self.h_layout_frame_title.addWidget(self.label_pust)

        self.label_sum = label_titul_f("сумма", self.frame_title)
        self.label_sum.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_sum)

        self.label_quantity = label_titul_f("количество", self.frame_title)
        self.label_quantity.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_quantity)

        self.label_tariff = label_titul_f("тариф", self.frame_title)
        self.label_tariff.setMinimumSize(QtCore.QSize(50, 18))
        self.h_layout_frame_title.addWidget(self.label_tariff)

        style = """
            QScrollBar:vertical {
            border: 2px solid grey;
            background: #32CC99;
            width: 20px;
            margin: 0 0 0 0;}
            """

        self.scrollArea = QtWidgets.QScrollArea(self.payments_group)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setStyleSheet("border: 1px solid rgba(209, 209, 217, 240);")
        self.scrollArea.setStyleSheet(style)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        # self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(760, 500))
        # self.scrollAreaWidgetContents.setStyleSheet("border: 0px solid rgba(209, 209, 217, 240);")
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # self.v_layout_scrollArea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.v_layout_scrollArea = QtWidgets.QVBoxLayout(self.scrollArea)
        self.v_layout_scrollArea.setContentsMargins(0, 0, 0, 5)
        self.v_layout_scrollArea.setObjectName("v_layout_scrollArea")

        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.v_layout_pay_group.addWidget(self.scrollArea)

        # # РАЗДЕЛИТЕЛЬ между основными и дополнительными платежами
        # self.LINE_RAZDEL = QtWidgets.QFrame(self.centralwidget)
        # self.LINE_RAZDEL.setGeometry(QtCore.QRect(10, 190, 760, 10))
        # # self.LINE_RAZDEL.setFixedSize(QtCore.QSize(760, 10))
        # self.LINE_RAZDEL.setAutoFillBackground(False)
        # self.LINE_RAZDEL.setStyleSheet("")
        # self.LINE_RAZDEL.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.LINE_RAZDEL.setLineWidth(1)
        # self.LINE_RAZDEL.setMidLineWidth(1)
        # self.LINE_RAZDEL.setFrameShape(QtWidgets.QFrame.HLine)
        # self.LINE_RAZDEL.setObjectName("LINE_RAZDEL")
        # self.g_layout_group_box.addWidget(self.LINE_RAZDEL, 9, 0, 1, 1)

        # Button Add Payment

        self.btn_add_payment = btn_f("Добавить платеж", self.WinPayment, 780, 35, 11)
        self.v_Layout_centralwidget.addWidget(self.btn_add_payment)

        # Frame Result

        self.frame_result = QtWidgets.QFrame(self.centralwidget)
        self.frame_result.setFixedSize(QtCore.QSize(780, 50))
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

        (self.frame_ui_footer, self.comboBox_month_CP, self.comboBox_year_CP, self.label_error_CP,
         self.btn_Save_CP, self.btn_Cancel_CP) = self.ui_head_foot.ui_win_footer(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_footer)

        QtCore.QMetaObject.connectSlotsByName(self.WinPayment)
        self.WinPayment.setTabOrder(self.btn_Right_CP, self.btn_add_payment)
        self.WinPayment.setTabOrder(self.btn_add_payment, self.comboBox_month_CP)
        self.WinPayment.setTabOrder(self.comboBox_month_CP, self.comboBox_year_CP)
        self.WinPayment.setTabOrder(self.comboBox_year_CP, self.btn_Save_CP)
        # self.WinPayment.setTabOrder(self.comboBox_year_CP, self.label_error_CP)
        self.WinPayment.setTabOrder(self.btn_Save_CP, self.btn_Cancel_CP)
        self.WinPayment.setTabOrder(self.btn_Cancel_CP, self.btn_Left_CP)
        self.WinPayment.setTabOrder(self.btn_Left_CP, self.btn_Right_CP)
