# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 600)
        MainWindow.setGeometry(QtCore.QRect(260, 240, 1400, 600))
        MainWindow.setMinimumSize(QtCore.QSize(1400, 600))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle('ДОМАШНЯЯ БУХГАЛТЕРИЯ')
        MainWindow.setWindowIcon(QIcon('res/img/123.ico'))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.menu_Menu = QtWidgets.QMenu(self.menubar)
        self.menu_Menu.setObjectName("menu_Menu")

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.action_Win_Counters = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/img/Counters-icon.png"))
        self.action_Win_Counters.setIcon(icon)
        self.action_Win_Counters.setObjectName("action_Win_Counters")

        self.action_Win_Payments = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/img/Payments-icon.png"))
        self.action_Win_Payments.setIcon(icon)
        self.action_Win_Payments.setObjectName("action_Win_Payments")

        # self.action_DebitKredit = QtWidgets.QAction(MainWindow)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("LAST/IMG/dollar.png"))
        # self.action_DebitKredit.setIcon(icon)
        # self.action_DebitKredit.setObjectName("action_DebitKredit")

        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")

        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.menu_Menu.addAction(self.action_Win_Counters)
        self.menu_Menu.addAction(self.action_Win_Payments)
        # self.menu_Menu.addAction(self.action_DebitKredit)

        self.menubar.addAction(self.menu_Menu.menuAction())

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Win_Counters)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Win_Payments)
        self.toolBar.addSeparator()
        # self.toolBar.addAction(self.action_DebitKredit)
        self.toolBar.addSeparator()

        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Заголовок Месяца и Года
        self.label_month_year = QtWidgets.QLabel(MainWindow)
        self.label_month_year.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_month_year.setFont(font)
        self.label_month_year.setAutoFillBackground(False)
        self.label_month_year.setStyleSheet("border: 1px solid rgba(50, 50, 50, 240);"
                                            "background-color: rgb(162, 162, 162);")
        self.label_month_year.setAlignment(QtCore.Qt.AlignCenter)
        self.label_month_year.setObjectName("label_month_year")
        self.gridLayout.addWidget(self.label_month_year, 0, 0, 1, 2)

        # Слой с кнопками выбора окна
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout")

        # spacerItem_1 = QtWidgets.QSpacerItem(1920, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_1.addItem(spacerItem_1)

        self.gridLayout.addLayout(self.horizontalLayout_1, 1, 0, 1, 2)

        # Сводная таблица данных за Год
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setRowCount(5)
        # self.tableWidget.setColumnCount(13)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background - color: rgb(223, 223, 223);")
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)

        # Слой с кнопками выбора действия
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem_2 = QtWidgets.QSpacerItem(1920, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem_2)

        # # Кнопка ОЧИСТИТЬ
        # self.pushButton_clean = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_clean.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_clean.sizePolicy().hasHeightForWidth())
        # self.pushButton_clean.setSizePolicy(sizePolicy)
        # self.pushButton_clean.setMinimumSize(QtCore.QSize(100, 25))
        # self.pushButton_clean.setMaximumSize(QtCore.QSize(100, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.pushButton_clean.setFont(font)
        # self.pushButton_clean.setObjectName("pushButton_clean")
        # self.horizontalLayout_2.addWidget(self.pushButton_clean)

        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        # СТАТУС БАР
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ДОМАШНЯЯ БУХГАЛТЕРИЯ"))
        self.menu_File.setTitle(_translate("MainWindow", "Файл"))
        self.menu_Menu.setTitle(_translate("MainWindow", "Меню"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Win_Counters.setText(_translate("MainWindow", "Показания счетчиков"))
        self.action_Win_Payments.setText(_translate("MainWindow", "Коммунальные платежи"))
        # self.action_DebitKredit.setText(_translate("MainWindow", "Доходы/Расходы"))
        self.action_Exit.setText(_translate("MainWindow", "Выход"))
        # self.pushButton_clean.setText(_translate("MainWindow", "Очистить"))
