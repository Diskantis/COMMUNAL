# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from res.UIC_CLASS_COMM import label_titul_f, lineEdit_pokaz_f, UiWinHeaderFooter, UiWinGrouper


class UiWinCounters(object):
    def setupUi_COU(self, WinCounters):
        self.WinCounters = WinCounters  # окно
        self.WinCounters.setObjectName("WinCounters")
        self.WinCounters.setWindowModality(Qt.ApplicationModal)
        self.WinCounters.resize(800, 400)
        self.WinCounters.setGeometry(QtCore.QRect(560, 300, 800, 400))
        self.WinCounters.setMinimumSize(QtCore.QSize(800, 400))
        self.WinCounters.setMaximumSize(QtCore.QSize(800, 400))
        self.WinCounters.setWindowTitle('ПОКАЗАНИЯ СЧЕТЧИКОВ')
        self.WinCounters.setWindowIcon(QIcon('res/img/Counters-icon.png'))
        self.WinCounters.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.ui_head_foot = UiWinHeaderFooter()

        self.centralwidget = QtWidgets.QWidget(self.WinCounters)
        self.centralwidget.setObjectName("centralwidget")

        self.v_Layout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.v_Layout_centralwidget.setContentsMargins(10, 10, 10, 10)
        self.v_Layout_centralwidget.setSpacing(8)
        self.v_Layout_centralwidget.setObjectName("v_Layout_centralwidget")

        (self.frame_ui_header, self.btn_Left_COU, self.label_month_year_COU, self.btn_Right_COU,
         self.label_GL_V_1_COU, self.label_GL_V_2_COU) = self.ui_head_foot.ui_win_header(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_header)

        self.frame_group = QtWidgets.QFrame(self.centralwidget)
        self.frame_group.setMinimumSize(QtCore.QSize(780, 304))
        self.frame_group.setMaximumSize(QtCore.QSize(780, 310))
        self.frame_group.setObjectName("frame_group")

        self.h_Layout_frame_group = QtWidgets.QHBoxLayout(self.frame_group)
        self.h_Layout_frame_group.setContentsMargins(0, 0, 0, 0)
        self.h_Layout_frame_group.setSpacing(8)
        self.h_Layout_frame_group.setObjectName("h_Layout_frame_gr")

        self.v_Layout_centralwidget.addWidget(self.frame_group)

        (self.frame_ui_footer, self.comboBox_month_COU, self.comboBox_year_COU, self.label_error_COU,
         self.btn_Save_COU, self.btn_Cancel_COU) = self.ui_head_foot.ui_win_footer(self.centralwidget)
        self.v_Layout_centralwidget.addWidget(self.frame_ui_footer)

        color_p = "(0, 160, 0)"
        color_c = "(0, 170, 255)"
        color_h = "(255, 140, 0, 255)"
        color_g = "(150, 0, 150)"
        color_ras = "(209, 209, 217)"

        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        # POWER

        self.grPowerBox = UiWinGrouper("Электроэнергия", self.WinCounters.frame_group)
        self.WinCounters.h_Layout_frame_group.addWidget(self.grPowerBox.group_box)

        self.label_sche_P = label_titul_f("Р/С 181 820 562", self.grPowerBox.fr_line_ed, 12)
        self.label_sche_P.setFixedSize(QtCore.QSize(215, 30))
        self.label_sche_P.setStyleSheet("color: rgb(80, 80, 80); background-color: rgb(255, 255, 0); padding: .4em; "
                                        "border: 1px solid rgba(50, 50, 50, 240); border-radius: 4px;")
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.label_sche_P, 0, 0, 1, 1)

        self.label_pred_P = label_titul_f("предыдущие", self.grPowerBox.fr_line_ed)
        self.label_pred_P.setFixedSize(QtCore.QSize(100, 25))
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.label_pred_P, 3, 0, 1, 1)

        self.label_post_P = label_titul_f("последние", self.grPowerBox.fr_line_ed)
        self.label_post_P.setFixedSize(QtCore.QSize(100, 25))
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.label_post_P, 3, 1, 1, 1)

        self.lineEdit_pred_P = lineEdit_pokaz_f("", self.grPowerBox.fr_line_ed, color_p, grad_1, grad_2)
        self.lineEdit_pred_P.setMinimumSize(QtCore.QSize(100, 125))
        self.lineEdit_pred_P.setMaximumSize(QtCore.QSize(100, 150))
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_P, 4, 0, 1, 1)

        self.lineEdit_post_P = lineEdit_pokaz_f("", self.grPowerBox.fr_line_ed, color_p, grad_2, grad_1)
        self.lineEdit_post_P.setMinimumSize(QtCore.QSize(100, 125))
        self.lineEdit_post_P.setMaximumSize(QtCore.QSize(100, 150))
        self.lineEdit_post_P.setReadOnly(False)
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_P, 4, 1, 1, 1)

        self.label_month_P = label_titul_f("месячный расход", self.grPowerBox.fr_line_ed)
        self.label_month_P.setMinimumSize(QtCore.QSize(210, 25))
        self.label_month_P.setMaximumSize(QtCore.QSize(210, 25))
        self.grPowerBox.g_layout_fr_line_ed.addWidget(self.label_month_P, 8, 0, 1, 1)

        self.label_month_ras_P = lineEdit_pokaz_f("", self.grPowerBox.fr_month_ras, color_ras, grad_1, grad_2)
        self.label_month_ras_P.setFixedSize(QtCore.QSize(214, 30))
        self.label_month_ras_P.setReadOnly(True)
        self.grPowerBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_P)

        # WATER

        self.grWaterBox = UiWinGrouper("Вода", self.WinCounters.frame_group)
        self.grWaterBox.group_box.setMinimumSize(QtCore.QSize(300, 300))
        self.WinCounters.h_Layout_frame_group.addWidget(self.grWaterBox.group_box)

        self.label_sche_W = label_titul_f("Р/С 300 046 056 19", self.grWaterBox.fr_line_ed, 12)
        self.label_sche_W.setMinimumSize(QtCore.QSize(100, 30))
        self.label_sche_W.setMaximumSize(QtCore.QSize(280, 30))
        self.label_sche_W.setStyleSheet("color: rgb(80, 80, 80); background-color: rgb(0, 170, 255); padding: .4em; "
                                        "border: 1px solid rgba(50, 50, 50, 240); border-radius: 4px;")
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W, 0, 0, 1, 3)

        self.label_sche_W = label_titul_f("счетчик", self.grWaterBox.fr_line_ed)
        self.label_sche_W.setMinimumSize(QtCore.QSize(80, 25))
        self.label_sche_W.setMaximumSize(QtCore.QSize(80, 25))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W, 3, 0, 1, 1)

        self.label_pred_W = label_titul_f("предыдущие", self.grWaterBox.fr_line_ed)
        self.label_pred_W.setMinimumSize(QtCore.QSize(90, 25))
        self.label_pred_W.setMaximumSize(QtCore.QSize(100, 25))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_pred_W, 3, 1, 1, 1)

        self.label_post_W = label_titul_f("последние", self.grWaterBox.fr_line_ed)
        self.label_post_W.setMinimumSize(QtCore.QSize(90, 25))
        self.label_post_W.setMaximumSize(QtCore.QSize(100, 25))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_post_W, 3, 2, 1, 1)

        self.label_sche_W1 = label_titul_f("№1 Туалет", self.grWaterBox.fr_line_ed)
        self.label_sche_W1.setMinimumSize(QtCore.QSize(80, 27))
        self.label_sche_W1.setMaximumSize(QtCore.QSize(80, 27))
        self.label_sche_W1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W1, 4, 0, 1, 1)

        self.lineEdit_pred_W1 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_c, grad_1, grad_2)
        self.lineEdit_pred_W1.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_pred_W1.setMaximumSize(QtCore.QSize(100, 27))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_W1, 4, 1, 1, 1)

        self.lineEdit_post_W1 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_c, grad_2, grad_1)
        self.lineEdit_post_W1.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_post_W1.setMaximumSize(QtCore.QSize(100, 27))
        self.lineEdit_post_W1.setReadOnly(False)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_W1, 4, 2, 1, 1)

        self.label_sche_W2 = label_titul_f("№2 Туалет", self.grWaterBox.fr_line_ed)
        self.label_sche_W2.setMinimumSize(QtCore.QSize(80, 27))
        self.label_sche_W2.setMaximumSize(QtCore.QSize(80, 27))
        self.label_sche_W2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W2, 5, 0, 1, 1)

        self.lineEdit_pred_W2 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_h, grad_1, grad_2)
        self.lineEdit_pred_W2.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_pred_W2.setMaximumSize(QtCore.QSize(100, 27))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_W2, 5, 1, 1, 1)

        self.lineEdit_post_W2 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_h, grad_2, grad_1)
        self.lineEdit_post_W2.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_post_W2.setMaximumSize(QtCore.QSize(100, 27))
        self.lineEdit_post_W2.setReadOnly(False)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_W2, 5, 2, 1, 1)

        self.label_sche_W3 = label_titul_f("№3 Кухня", self.grWaterBox.fr_line_ed)
        self.label_sche_W3.setMinimumSize(QtCore.QSize(80, 27))
        self.label_sche_W3.setMaximumSize(QtCore.QSize(80, 27))
        self.label_sche_W3.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W3, 6, 0, 1, 1)

        self.lineEdit_pred_W3 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_c, grad_1, grad_2)
        self.lineEdit_pred_W3.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_pred_W3.setMaximumSize(QtCore.QSize(100, 27))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_W3, 6, 1, 1, 1)

        self.lineEdit_post_W3 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_c, grad_2, grad_1)
        self.lineEdit_post_W3.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_post_W3.setMaximumSize(QtCore.QSize(100, 27))
        self.lineEdit_post_W3.setReadOnly(False)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_W3, 6, 2, 1, 1)

        self.label_sche_W4 = label_titul_f("№4 Кухня", self.grWaterBox.fr_line_ed)
        self.label_sche_W4.setMinimumSize(QtCore.QSize(80, 27))
        self.label_sche_W4.setMaximumSize(QtCore.QSize(80, 27))
        self.label_sche_W4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_sche_W4, 7, 0, 1, 1)

        self.lineEdit_pred_W4 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_h, grad_1, grad_2)
        self.lineEdit_pred_W4.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_pred_W4.setMaximumSize(QtCore.QSize(100, 27))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_W4, 7, 1, 1, 1)

        self.lineEdit_post_W4 = lineEdit_pokaz_f("", self.grWaterBox.fr_line_ed, color_h, grad_2, grad_1)
        self.lineEdit_post_W4.setMinimumSize(QtCore.QSize(90, 27))
        self.lineEdit_post_W4.setMaximumSize(QtCore.QSize(100, 27))
        self.lineEdit_post_W4.setReadOnly(False)
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_W4, 7, 2, 1, 1)

        self.label_month_W = label_titul_f("месячный расход", self.grWaterBox.fr_line_ed)
        self.label_month_W.setMinimumSize(QtCore.QSize(100, 25))
        self.label_month_W.setMaximumSize(QtCore.QSize(280, 25))
        self.grWaterBox.g_layout_fr_line_ed.addWidget(self.label_month_W, 8, 0, 1, 3)

        self.grWaterBox.fr_month_ras.setMinimumSize(QtCore.QSize(280, 0))

        self.label_month_ras_WC = lineEdit_pokaz_f("", self.grWaterBox.fr_month_ras, color_c, grad_1, grad_2)
        self.label_month_ras_WC.setFixedSize(QtCore.QSize(70, 30))
        self.grWaterBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_WC)

        self.label_month_ras_PLUS = label_titul_f("+", self.grWaterBox.fr_line_ed)
        self.label_month_ras_PLUS.setFixedSize(QtCore.QSize(22, 30))
        self.grWaterBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_PLUS)

        self.label_month_ras_WH = lineEdit_pokaz_f("", self.grWaterBox.fr_month_ras, color_h, grad_1, grad_2)
        self.label_month_ras_WH.setFixedSize(QtCore.QSize(70, 30))
        self.grWaterBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_WH)

        self.label_month_ras_SUMM = label_titul_f("=", self.grWaterBox.fr_line_ed)
        self.label_month_ras_SUMM.setFixedSize(QtCore.QSize(22, 30))
        self.grWaterBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_SUMM)

        self.label_month_ras_W = lineEdit_pokaz_f("", self.grWaterBox.fr_month_ras, color_ras, grad_1, grad_2)
        self.label_month_ras_W.setFixedSize(QtCore.QSize(74, 30))
        self.grWaterBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_W)

        # GAZ

        self.grGazBox = UiWinGrouper("Газ", self.WinCounters.frame_group)
        self.WinCounters.h_Layout_frame_group.addWidget(self.grGazBox.group_box)

        self.label_sche_G = label_titul_f("Р/С 171 269 - 5", self.grGazBox.fr_line_ed, 12)
        self.label_sche_G.setFixedSize(QtCore.QSize(215, 30))
        self.label_sche_G.setStyleSheet("color: rgb(80, 80, 80); background-color: rgb(255, 85, 255); padding: .4em; "
                                        "border: 1px solid rgba(50, 50, 50, 240); border-radius: 4px;")
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.label_sche_G, 0, 0, 1, 1)

        self.label_pred_G = label_titul_f("предыдущие", self.grGazBox.fr_line_ed)
        self.label_pred_G.setFixedSize(QtCore.QSize(100, 25))
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.label_pred_G, 3, 0, 1, 1)

        self.label_post_G = label_titul_f("последние", self.grGazBox.fr_line_ed)
        self.label_post_G.setFixedSize(QtCore.QSize(100, 25))
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.label_post_G, 3, 1, 1, 1)

        self.lineEdit_pred_G = lineEdit_pokaz_f("", self.grGazBox.fr_line_ed, color_g, grad_1, grad_2)
        self.lineEdit_pred_G.setMinimumSize(QtCore.QSize(100, 125))
        self.lineEdit_pred_G.setMaximumSize(QtCore.QSize(100, 150))
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.lineEdit_pred_G, 4, 0, 1, 1)

        self.lineEdit_post_G = lineEdit_pokaz_f("", self.grGazBox.fr_line_ed, color_g, grad_2, grad_1)
        self.lineEdit_post_G.setMinimumSize(QtCore.QSize(100, 125))
        self.lineEdit_post_G.setMaximumSize(QtCore.QSize(100, 150))
        self.lineEdit_post_G.setReadOnly(False)
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.lineEdit_post_G, 4, 1, 1, 1)

        self.label_month_G = label_titul_f("месячный расход", self.grGazBox.fr_line_ed)
        self.label_month_G.setMinimumSize(QtCore.QSize(210, 25))
        self.label_month_G.setMaximumSize(QtCore.QSize(210, 25))
        self.grGazBox.g_layout_fr_line_ed.addWidget(self.label_month_G, 8, 0, 1, 1)

        self.label_month_ras_G = lineEdit_pokaz_f("", self.grGazBox.fr_month_ras, color_ras, grad_1, grad_2)
        self.label_month_ras_G.setFixedSize(QtCore.QSize(214, 30))
        self.label_month_ras_G.setReadOnly(True)
        self.grGazBox.h_layout_fr_month_ras.addWidget(self.label_month_ras_G)

        QtCore.QMetaObject.connectSlotsByName(self.WinCounters)
        self.WinCounters.setTabOrder(self.comboBox_month_COU, self.comboBox_year_COU)
        self.WinCounters.setTabOrder(self.comboBox_year_COU, self.btn_Left_COU)
        self.WinCounters.setTabOrder(self.btn_Left_COU, self.btn_Right_COU)
        self.WinCounters.setTabOrder(self.btn_Right_COU, self.lineEdit_post_P)
        self.WinCounters.setTabOrder(self.lineEdit_post_P, self.lineEdit_post_W1)
        self.WinCounters.setTabOrder(self.lineEdit_post_W1, self.lineEdit_post_W2)
        self.WinCounters.setTabOrder(self.lineEdit_post_W2, self.lineEdit_post_W3)
        self.WinCounters.setTabOrder(self.lineEdit_post_W3, self.lineEdit_post_W4)
        self.WinCounters.setTabOrder(self.lineEdit_post_W4, self.lineEdit_post_G)
        self.WinCounters.setTabOrder(self.lineEdit_post_G, self.btn_Save_COU)
        self.WinCounters.setTabOrder(self.btn_Save_COU, self.btn_Cancel_COU)
        self.WinCounters.setTabOrder(self.btn_Cancel_COU, self.lineEdit_pred_P)
        self.WinCounters.setTabOrder(self.lineEdit_pred_P, self.lineEdit_pred_W1)
        self.WinCounters.setTabOrder(self.lineEdit_pred_W1, self.lineEdit_pred_W2)
        self.WinCounters.setTabOrder(self.lineEdit_pred_W2, self.lineEdit_pred_W3)
        self.WinCounters.setTabOrder(self.lineEdit_pred_W3, self.lineEdit_pred_W4)
        self.WinCounters.setTabOrder(self.lineEdit_pred_W4, self.lineEdit_pred_G)
        self.WinCounters.setTabOrder(self.lineEdit_pred_G, self.label_month_ras_P)
        self.WinCounters.setTabOrder(self.label_month_ras_P, self.label_month_ras_WC)
        self.WinCounters.setTabOrder(self.label_month_ras_WC, self.label_month_ras_WH)
        self.WinCounters.setTabOrder(self.label_month_ras_WH, self.label_month_ras_W)
        self.WinCounters.setTabOrder(self.label_month_ras_W, self.label_month_ras_G)
        self.WinCounters.setTabOrder(self.label_month_ras_G, self.comboBox_month_COU)
