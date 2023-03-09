# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1528, 779)
        icon = QIcon()
        icon.addFile(u"image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Pomiary = QWidget()
        self.Pomiary.setObjectName(u"Pomiary")
        self.gridLayout = QGridLayout(self.Pomiary)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.Pomiary)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 24, 1, 2)

        self.pushButton_6 = QPushButton(self.Pomiary)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 6, 27, 1, 2)

        self.ilR = QSpinBox(self.Pomiary)
        self.ilR.setObjectName(u"ilR")
        self.ilR.setMaximumSize(QSize(30, 16777215))
        self.ilR.setMaximum(10)
        self.ilR.setValue(6)

        self.gridLayout.addWidget(self.ilR, 1, 23, 1, 1)

        self.Wyczysc = QPushButton(self.Pomiary)
        self.Wyczysc.setObjectName(u"Wyczysc")
        self.Wyczysc.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.Wyczysc, 6, 7, 1, 2)

        self.sciezka_Model = QLineEdit(self.Pomiary)
        self.sciezka_Model.setObjectName(u"sciezka_Model")

        self.gridLayout.addWidget(self.sciezka_Model, 1, 25, 3, 3)

        self.tabWidget_2 = QTabWidget(self.Pomiary)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.DCV = QWidget()
        self.DCV.setObjectName(u"DCV")
        self.gridLayout_2 = QGridLayout(self.DCV)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_21 = QPushButton(self.DCV)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_2.addWidget(self.pushButton_21, 6, 5, 1, 1)

        self.label_3 = QLabel(self.DCV)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 5, 1, 1)

        self.pushButton_20 = QPushButton(self.DCV)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_2.addWidget(self.pushButton_20, 5, 5, 1, 1)

        self.pushButton = QPushButton(self.DCV)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 4, 5, 1, 1)

        self.wynikiDCV = QTableWidget(self.DCV)
        self.wynikiDCV.setObjectName(u"wynikiDCV")

        self.gridLayout_2.addWidget(self.wynikiDCV, 0, 0, 8, 1)

        self.pushButton_7 = QPushButton(self.DCV)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 7, 5, 1, 1)

        self.tabWidget_2.addTab(self.DCV, "")
        self.ACV = QWidget()
        self.ACV.setObjectName(u"ACV")
        self.gridLayout_3 = QGridLayout(self.ACV)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_22 = QPushButton(self.ACV)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_3.addWidget(self.pushButton_22, 7, 5, 1, 1)

        self.wynikiACV = QTableWidget(self.ACV)
        self.wynikiACV.setObjectName(u"wynikiACV")

        self.gridLayout_3.addWidget(self.wynikiACV, 0, 1, 8, 1)

        self.pushButton_24 = QPushButton(self.ACV)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_3.addWidget(self.pushButton_24, 6, 5, 1, 1)

        self.pushButton_23 = QPushButton(self.ACV)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_3.addWidget(self.pushButton_23, 5, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.ACV)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 4, 5, 1, 1)

        self.label_19 = QLabel(self.ACV)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_19, 2, 5, 1, 1)

        self.tabWidget_2.addTab(self.ACV, "")
        self.DCI = QWidget()
        self.DCI.setObjectName(u"DCI")
        self.gridLayout_4 = QGridLayout(self.DCI)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_26 = QPushButton(self.DCI)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_4.addWidget(self.pushButton_26, 2, 3, 1, 1)

        self.pushButton_25 = QPushButton(self.DCI)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_4.addWidget(self.pushButton_25, 4, 3, 1, 1)

        self.pushButton_27 = QPushButton(self.DCI)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_4.addWidget(self.pushButton_27, 3, 3, 1, 1)

        self.label_4 = QLabel(self.DCI)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 2)

        self.pushButton_3 = QPushButton(self.DCI)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.wynikiDCI = QTableWidget(self.DCI)
        self.wynikiDCI.setObjectName(u"wynikiDCI")

        self.gridLayout_4.addWidget(self.wynikiDCI, 0, 1, 5, 1)

        self.tabWidget_2.addTab(self.DCI, "")
        self.ACI = QWidget()
        self.ACI.setObjectName(u"ACI")
        self.gridLayout_5 = QGridLayout(self.ACI)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.ACI)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 0, 2, 1, 2)

        self.pushButton_30 = QPushButton(self.ACI)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_5.addWidget(self.pushButton_30, 3, 3, 1, 1)

        self.pushButton_29 = QPushButton(self.ACI)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_5.addWidget(self.pushButton_29, 2, 3, 1, 1)

        self.pushButton_28 = QPushButton(self.ACI)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_5.addWidget(self.pushButton_28, 4, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.ACI)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.wynikiACI = QTableWidget(self.ACI)
        self.wynikiACI.setObjectName(u"wynikiACI")

        self.gridLayout_5.addWidget(self.wynikiACI, 0, 1, 5, 1)

        self.tabWidget_2.addTab(self.ACI, "")
        self.R = QWidget()
        self.R.setObjectName(u"R")
        self.gridLayout_6 = QGridLayout(self.R)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_31 = QPushButton(self.R)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.gridLayout_6.addWidget(self.pushButton_31, 1, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.R)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.gridLayout_6.addWidget(self.pushButton_32, 1, 1, 1, 1)

        self.wynikiR = QTableWidget(self.R)
        self.wynikiR.setObjectName(u"wynikiR")

        self.gridLayout_6.addWidget(self.wynikiR, 0, 0, 1, 3)

        self.tabWidget_2.addTab(self.R, "")

        self.gridLayout.addWidget(self.tabWidget_2, 5, 0, 1, 32)

        self.label_9 = QLabel(self.Pomiary)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.Pomiary)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 6, 29, 1, 2)

        self.ilACV = QSpinBox(self.Pomiary)
        self.ilACV.setObjectName(u"ilACV")
        self.ilACV.setMaximumSize(QSize(30, 16777215))
        self.ilACV.setMaximum(10)
        self.ilACV.setValue(2)

        self.gridLayout.addWidget(self.ilACV, 1, 17, 1, 1)

        self.check_acv = QCheckBox(self.Pomiary)
        self.check_acv.setObjectName(u"check_acv")
        self.check_acv.setChecked(True)

        self.gridLayout.addWidget(self.check_acv, 1, 16, 1, 1)

        self.check_aci = QCheckBox(self.Pomiary)
        self.check_aci.setObjectName(u"check_aci")
        self.check_aci.setChecked(True)

        self.gridLayout.addWidget(self.check_aci, 1, 19, 1, 1)

        self.ilDCV = QSpinBox(self.Pomiary)
        self.ilDCV.setObjectName(u"ilDCV")
        self.ilDCV.setMinimumSize(QSize(0, 0))
        self.ilDCV.setMaximumSize(QSize(30, 16777215))
        self.ilDCV.setMaximum(10)
        self.ilDCV.setValue(5)

        self.gridLayout.addWidget(self.ilDCV, 1, 7, 1, 1)

        self.wartosc_kalibrator = QDoubleSpinBox(self.Pomiary)
        self.wartosc_kalibrator.setObjectName(u"wartosc_kalibrator")
        self.wartosc_kalibrator.setMaximum(1001.000000000000000)

        self.gridLayout.addWidget(self.wartosc_kalibrator, 6, 1, 1, 1)

        self.odczyt_kalibrator = QLineEdit(self.Pomiary)
        self.odczyt_kalibrator.setObjectName(u"odczyt_kalibrator")
        self.odczyt_kalibrator.setEnabled(True)
        self.odczyt_kalibrator.setDragEnabled(False)
        self.odczyt_kalibrator.setReadOnly(True)

        self.gridLayout.addWidget(self.odczyt_kalibrator, 6, 26, 1, 1)

        self.Stworz = QPushButton(self.Pomiary)
        self.Stworz.setObjectName(u"Stworz")

        self.gridLayout.addWidget(self.Stworz, 1, 28, 3, 2)

        self.AC_DC = QComboBox(self.Pomiary)
        self.AC_DC.addItem("")
        self.AC_DC.addItem("")
        self.AC_DC.setObjectName(u"AC_DC")
        self.AC_DC.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.AC_DC, 6, 4, 1, 1)

        self.zamkniecie_aplikacji = QPushButton(self.Pomiary)
        self.zamkniecie_aplikacji.setObjectName(u"zamkniecie_aplikacji")
        self.zamkniecie_aplikacji.setToolTipDuration(8)

        self.gridLayout.addWidget(self.zamkniecie_aplikacji, 6, 31, 1, 1)

        self.Nastaw = QPushButton(self.Pomiary)
        self.Nastaw.setObjectName(u"Nastaw")
        self.Nastaw.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.Nastaw, 6, 5, 1, 1)

        self.check_dci = QCheckBox(self.Pomiary)
        self.check_dci.setObjectName(u"check_dci")
        self.check_dci.setChecked(True)

        self.gridLayout.addWidget(self.check_dci, 1, 10, 1, 3)

        self.ilACI = QSpinBox(self.Pomiary)
        self.ilACI.setObjectName(u"ilACI")
        self.ilACI.setMaximumSize(QSize(30, 16777215))
        self.ilACI.setMaximum(10)
        self.ilACI.setValue(3)

        self.gridLayout.addWidget(self.ilACI, 1, 20, 1, 1)

        self.check_r = QCheckBox(self.Pomiary)
        self.check_r.setObjectName(u"check_r")
        self.check_r.setChecked(True)

        self.gridLayout.addWidget(self.check_r, 1, 22, 1, 1)

        self.SzukajModelu = QPushButton(self.Pomiary)
        self.SzukajModelu.setObjectName(u"SzukajModelu")

        self.gridLayout.addWidget(self.SzukajModelu, 1, 30, 3, 2)

        self.label_12 = QLabel(self.Pomiary)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 3, 1, 2)

        self.check_dcv = QCheckBox(self.Pomiary)
        self.check_dcv.setObjectName(u"check_dcv")
        self.check_dcv.setChecked(True)

        self.gridLayout.addWidget(self.check_dcv, 1, 5, 1, 1)

        self.label_6 = QLabel(self.Pomiary)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 0))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.ilDCI = QSpinBox(self.Pomiary)
        self.ilDCI.setObjectName(u"ilDCI")
        self.ilDCI.setMaximumSize(QSize(30, 16777215))
        self.ilDCI.setMaximum(10)
        self.ilDCI.setValue(4)

        self.gridLayout.addWidget(self.ilDCI, 1, 14, 1, 1)

        self.label = QLabel(self.Pomiary)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"image/tlo_poloficial.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 32)

        self.ustawienie_kalibrator = QComboBox(self.Pomiary)
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.setObjectName(u"ustawienie_kalibrator")

        self.gridLayout.addWidget(self.ustawienie_kalibrator, 6, 2, 1, 2)

        self.comboBox = QComboBox(self.Pomiary)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 2)

        self.zakresR = QSpinBox(self.Pomiary)
        self.zakresR.setObjectName(u"zakresR")
        self.zakresR.setMinimumSize(QSize(60, 0))
        self.zakresR.setMaximum(500000000)
        self.zakresR.setValue(200000000)
        self.zakresR.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.zakresR, 2, 22, 1, 2)

        self.zakresACI_2 = QDoubleSpinBox(self.Pomiary)
        self.zakresACI_2.setObjectName(u"zakresACI_2")
        self.zakresACI_2.setMaximumSize(QSize(50, 16777215))
        self.zakresACI_2.setMaximum(1000.000000000000000)
        self.zakresACI_2.setValue(0.400000000000000)

        self.gridLayout.addWidget(self.zakresACI_2, 2, 20, 1, 1)

        self.zakresACI = QSpinBox(self.Pomiary)
        self.zakresACI.setObjectName(u"zakresACI")
        self.zakresACI.setMinimumSize(QSize(50, 0))
        self.zakresACI.setMaximum(1000)
        self.zakresACI.setValue(10)

        self.gridLayout.addWidget(self.zakresACI, 2, 19, 1, 1)

        self.label_54 = QLabel(self.Pomiary)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout.addWidget(self.label_54, 2, 21, 1, 1)

        self.zakresACV_ = QDoubleSpinBox(self.Pomiary)
        self.zakresACV_.setObjectName(u"zakresACV_")
        self.zakresACV_.setMaximumSize(QSize(60, 16777210))
        self.zakresACV_.setMaximum(1000.000000000000000)
        self.zakresACV_.setValue(400.000000000000000)

        self.gridLayout.addWidget(self.zakresACV_, 2, 17, 1, 1)

        self.label_53 = QLabel(self.Pomiary)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout.addWidget(self.label_53, 2, 18, 2, 1)

        self.label_17 = QLabel(self.Pomiary)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 2, 24, 2, 1)

        self.zakresACV = QSpinBox(self.Pomiary)
        self.zakresACV.setObjectName(u"zakresACV")
        self.zakresACV.setMinimumSize(QSize(50, 0))
        self.zakresACV.setMaximum(1000)
        self.zakresACV.setValue(750)

        self.gridLayout.addWidget(self.zakresACV, 2, 16, 1, 1)

        self.zakresDCV = QSpinBox(self.Pomiary)
        self.zakresDCV.setObjectName(u"zakresDCV")
        self.zakresDCV.setMinimumSize(QSize(0, 0))
        self.zakresDCV.setMaximumSize(QSize(50, 16777215))
        self.zakresDCV.setMaximum(1000)
        self.zakresDCV.setValue(1000)

        self.gridLayout.addWidget(self.zakresDCV, 2, 5, 1, 1)

        self.zakresDCV_2 = QDoubleSpinBox(self.Pomiary)
        self.zakresDCV_2.setObjectName(u"zakresDCV_2")
        self.zakresDCV_2.setMaximumSize(QSize(60, 16777215))
        self.zakresDCV_2.setMaximum(1000.000000000000000)
        self.zakresDCV_2.setValue(400.000000000000000)

        self.gridLayout.addWidget(self.zakresDCV_2, 2, 7, 1, 1)

        self.zakresDCI = QSpinBox(self.Pomiary)
        self.zakresDCI.setObjectName(u"zakresDCI")
        self.zakresDCI.setMinimumSize(QSize(50, 0))
        self.zakresDCI.setMaximum(1000)
        self.zakresDCI.setValue(10)

        self.gridLayout.addWidget(self.zakresDCI, 2, 10, 1, 3)

        self.zakresDCI_2 = QDoubleSpinBox(self.Pomiary)
        self.zakresDCI_2.setObjectName(u"zakresDCI_2")
        self.zakresDCI_2.setMaximumSize(QSize(50, 16777215))
        self.zakresDCI_2.setMaximum(1000.000000000000000)
        self.zakresDCI_2.setValue(0.400000000000000)

        self.gridLayout.addWidget(self.zakresDCI_2, 2, 14, 1, 1)

        self.label_14 = QLabel(self.Pomiary)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 8, 2, 2)

        self.label_15 = QLabel(self.Pomiary)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 15, 2, 1)

        self.label_13 = QLabel(self.Pomiary)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 3, 1, 2)

        self.tabWidget.addTab(self.Pomiary, "")
        self.Swiadectwo = QWidget()
        self.Swiadectwo.setObjectName(u"Swiadectwo")
        self.gridLayout_7 = QGridLayout(self.Swiadectwo)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Wybor_zglaszajacy = QComboBox(self.Swiadectwo)
        self.Wybor_zglaszajacy.addItem("")
        self.Wybor_zglaszajacy.addItem("")
        self.Wybor_zglaszajacy.addItem("")
        self.Wybor_zglaszajacy.setObjectName(u"Wybor_zglaszajacy")

        self.gridLayout_7.addWidget(self.Wybor_zglaszajacy, 5, 2, 1, 1)

        self.label_35 = QLabel(self.Swiadectwo)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_7.addWidget(self.label_35, 14, 3, 1, 1)

        self.label_7 = QLabel(self.Swiadectwo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"image/tlo_poloficial.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 8)

        self.data_wzorcowania = QDateEdit(self.Swiadectwo)
        self.data_wzorcowania.setObjectName(u"data_wzorcowania")
        self.data_wzorcowania.setDateTime(QDateTime(QDate(2023, 2, 9), QTime(17, 0, 0)))
        self.data_wzorcowania.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.data_wzorcowania, 2, 0, 2, 1)

        self.label_25 = QLabel(self.Swiadectwo)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 1, 2, 1, 1)

        self.SzukajWynikow = QPushButton(self.Swiadectwo)
        self.SzukajWynikow.setObjectName(u"SzukajWynikow")
        self.SzukajWynikow.setEnabled(True)
        self.SzukajWynikow.setMinimumSize(QSize(0, 24))
        self.SzukajWynikow.setMaximumSize(QSize(100, 16777215))
        self.SzukajWynikow.setBaseSize(QSize(0, 0))
        self.SzukajWynikow.setAutoRepeatDelay(300)

        self.gridLayout_7.addWidget(self.SzukajWynikow, 15, 4, 1, 1)

        self.label_28 = QLabel(self.Swiadectwo)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 11, 3, 1, 1)

        self.niepewnosc_pomiaru = QTextEdit(self.Swiadectwo)
        self.niepewnosc_pomiaru.setObjectName(u"niepewnosc_pomiaru")
        self.niepewnosc_pomiaru.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.niepewnosc_pomiaru, 12, 0, 1, 1)

        self.wyniki_wzorcowania = QTableWidget(self.Swiadectwo)
        self.wyniki_wzorcowania.setObjectName(u"wyniki_wzorcowania")
        self.wyniki_wzorcowania.setMinimumSize(QSize(700, 400))

        self.gridLayout_7.addWidget(self.wyniki_wzorcowania, 2, 4, 12, 4)

        self.ANG = QRadioButton(self.Swiadectwo)
        self.ANG.setObjectName(u"ANG")

        self.gridLayout_7.addWidget(self.ANG, 1, 3, 2, 1)

        self.label_31 = QLabel(self.Swiadectwo)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 11, 0, 1, 1)

        self.label_27 = QLabel(self.Swiadectwo)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 5, 3, 1, 1)

        self.odczyt_wynikow = QPushButton(self.Swiadectwo)
        self.odczyt_wynikow.setObjectName(u"odczyt_wynikow")
        self.odczyt_wynikow.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.odczyt_wynikow, 15, 5, 1, 1)

        self.sciezkaSW_zapis = QLineEdit(self.Swiadectwo)
        self.sciezkaSW_zapis.setObjectName(u"sciezkaSW_zapis")
        self.sciezkaSW_zapis.setMinimumSize(QSize(0, 0))

        self.gridLayout_7.addWidget(self.sciezkaSW_zapis, 15, 0, 1, 1)

        self.spojnosc_pomiarowa = QTextEdit(self.Swiadectwo)
        self.spojnosc_pomiarowa.setObjectName(u"spojnosc_pomiarowa")

        self.gridLayout_7.addWidget(self.spojnosc_pomiarowa, 12, 2, 1, 1)

        self.label_11 = QLabel(self.Swiadectwo)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 4, 2, 1, 1)

        self.sciezkaWynik_zapis = QLineEdit(self.Swiadectwo)
        self.sciezkaWynik_zapis.setObjectName(u"sciezkaWynik_zapis")

        self.gridLayout_7.addWidget(self.sciezkaWynik_zapis, 15, 3, 1, 1)

        self.generuj_swiadectwo = QPushButton(self.Swiadectwo)
        self.generuj_swiadectwo.setObjectName(u"generuj_swiadectwo")

        self.gridLayout_7.addWidget(self.generuj_swiadectwo, 15, 7, 1, 1)

        self.Zglaszajacy = QTextEdit(self.Swiadectwo)
        self.Zglaszajacy.setObjectName(u"Zglaszajacy")

        self.gridLayout_7.addWidget(self.Zglaszajacy, 7, 2, 1, 1)

        self.metoda_wzorcowania = QTextEdit(self.Swiadectwo)
        self.metoda_wzorcowania.setObjectName(u"metoda_wzorcowania")

        self.gridLayout_7.addWidget(self.metoda_wzorcowania, 7, 3, 1, 1)

        self.numer_swiadectwa = QLineEdit(self.Swiadectwo)
        self.numer_swiadectwa.setObjectName(u"numer_swiadectwa")
        self.numer_swiadectwa.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.numer_swiadectwa, 2, 2, 2, 1)

        self.SzukajSW = QPushButton(self.Swiadectwo)
        self.SzukajSW.setObjectName(u"SzukajSW")
        self.SzukajSW.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.SzukajSW, 15, 2, 1, 1)

        self.warunki_srodowiskowe = QTextEdit(self.Swiadectwo)
        self.warunki_srodowiskowe.setObjectName(u"warunki_srodowiskowe")

        self.gridLayout_7.addWidget(self.warunki_srodowiskowe, 12, 3, 1, 1)

        self.label_26 = QLabel(self.Swiadectwo)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_30 = QLabel(self.Swiadectwo)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 11, 2, 1, 1)

        self.label_2 = QLabel(self.Swiadectwo)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)

        self.przedmiot_wzorcowania = QTextEdit(self.Swiadectwo)
        self.przedmiot_wzorcowania.setObjectName(u"przedmiot_wzorcowania")

        self.gridLayout_7.addWidget(self.przedmiot_wzorcowania, 7, 0, 1, 1)

        self.label_34 = QLabel(self.Swiadectwo)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_7.addWidget(self.label_34, 14, 0, 1, 1)

        self.Zapisz_wynik = QPushButton(self.Swiadectwo)
        self.Zapisz_wynik.setObjectName(u"Zapisz_wynik")

        self.gridLayout_7.addWidget(self.Zapisz_wynik, 15, 6, 1, 1)

        self.label_33 = QLabel(self.Swiadectwo)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_7.addWidget(self.label_33, 1, 4, 1, 1)

        self.tabWidget.addTab(self.Swiadectwo, "")
        self.Informacje = QWidget()
        self.Informacje.setObjectName(u"Informacje")
        self.verticalLayout_2 = QVBoxLayout(self.Informacje)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.Informacje)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u"image/tlo_poloficial.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_8)

        self.textEdit = QTextEdit(self.Informacje)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.tabWidget.addTab(self.Informacje, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1528, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_25.setBuddy(self.numer_swiadectwa)
        self.label_2.setBuddy(self.data_wzorcowania)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.zamkniecie_aplikacji.clicked.connect(MainWindow.close)
        self.Wyczysc.clicked.connect(self.wartosc_kalibrator.clear)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiMeasure", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Odczytana warto\u015b\u0107:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Wyczysc.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_3.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.DCV), QCoreApplication.translate("MainWindow", u"DCV", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.label_19.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.ACV), QCoreApplication.translate("MainWindow", u"ACV", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_4.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.DCI), QCoreApplication.translate("MainWindow", u"DCI", None))
        self.label_5.setText("")
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.ACI), QCoreApplication.translate("MainWindow", u"ACI", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.R), QCoreApplication.translate("MainWindow", u"R", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ustaw warto\u015b\u0107:", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.check_acv.setText(QCoreApplication.translate("MainWindow", u"ACV", None))
        self.check_aci.setText(QCoreApplication.translate("MainWindow", u"ACI", None))
        self.odczyt_kalibrator.setInputMask("")
        self.odczyt_kalibrator.setText("")
        self.Stworz.setText(QCoreApplication.translate("MainWindow", u"Stw\u00f3rz", None))
        self.AC_DC.setItemText(0, QCoreApplication.translate("MainWindow", u"DC", None))
        self.AC_DC.setItemText(1, QCoreApplication.translate("MainWindow", u"AC", None))

        self.zamkniecie_aplikacji.setText(QCoreApplication.translate("MainWindow", u"Wyj\u015bcie", None))
        self.Nastaw.setText(QCoreApplication.translate("MainWindow", u"Nastaw", None))
        self.check_dci.setText(QCoreApplication.translate("MainWindow", u"DCI", None))
        self.check_r.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.SzukajModelu.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Lub Wybierz", None))
        self.check_dcv.setText(QCoreApplication.translate("MainWindow", u"DCV", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wybierz model:", None))
        self.label.setText("")
        self.ustawienie_kalibrator.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.ustawienie_kalibrator.setItemText(1, QCoreApplication.translate("MainWindow", u"V", None))
        self.ustawienie_kalibrator.setItemText(2, QCoreApplication.translate("MainWindow", u"mA", None))
        self.ustawienie_kalibrator.setItemText(3, QCoreApplication.translate("MainWindow", u"A", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Fluke 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Fluke 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fluke 3", None))

        self.label_54.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Podaj zakresy:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pomiary), QCoreApplication.translate("MainWindow", u"Pomiary", None))
        self.Wybor_zglaszajacy.setItemText(0, QCoreApplication.translate("MainWindow", u"Linetech", None))
        self.Wybor_zglaszajacy.setItemText(1, QCoreApplication.translate("MainWindow", u"Hanza", None))
        self.Wybor_zglaszajacy.setItemText(2, QCoreApplication.translate("MainWindow", u"Hitachi", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u015acie\u017cka zapisu wynik\u00f3w:", None))
        self.label_7.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Nr. \u015awiadectwa:", None))
        self.SzukajWynikow.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Warunki \u015arodowiskowe:", None))
        self.niepewnosc_pomiaru.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Niepewno\u015b\u0107 pomiaru zosta\u0142a okre\u015blona zgodnie z dokumentem EA-4/02 M:2021. Podane warto\u015bci niepewno\u015bci stanowi\u0105 niepewno\u015bci rozszerzone przy prawdopodobie\u0144stwie rozszerzenia ok. 95 % i wsp\u00f3\u0142czynniku rozszerzenia k = 2</p></body></html>", None))
        self.ANG.setText(QCoreApplication.translate("MainWindow", u"\u015a.W. po ang", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Niepewno\u015b\u0107 pomiaru:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Metoda wzorcowania:", None))
        self.odczyt_wynikow.setText(QCoreApplication.translate("MainWindow", u"Odczyt wynik\u00f3w", None))
        self.spojnosc_pomiarowa.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wyniki wzorcowania miernika zosta\u0142y odniesione do wzorc\u00f3w pa\u0144stwowych przy wykorzystaniu multimetru wzorcowego: ...</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Zg\u0142aszaj\u0105cy", None))
        self.generuj_swiadectwo.setText(QCoreApplication.translate("MainWindow", u"Generuj \u015awiadectwo", None))
        self.Zglaszajacy.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">LINETECH S.A.<br />ul. Warecka 11A<br />00-034 Warszawa</span></p></body></html>", None))
        self.metoda_wzorcowania.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Procedura pomiarowa PW005 wydanie 2</p></body></html>", None))
        self.numer_swiadectwa.setText(QCoreApplication.translate("MainWindow", u"9999/02/2023", None))
        self.SzukajSW.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.warunki_srodowiskowe.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temperatura (21 <a name=\"char-node\"></a><span style=\" font-family:'u0000';\">\u00f7</span> 23) \u00b0C</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wilgotno\u015b\u0107   (42 <a name=\"char-node\"></a><span style=\" font-family:'u0000';\">\u00f7</span> 47) %</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Przedmiot wzorcowania:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sp\u00f3jno\u015b\u0107 pomiarowa:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data wzorcowania:", None))
        self.przedmiot_wzorcowania.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Multimetr [MODEL], nr </span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u015acie\u017cka zapisu \u015bwiadectwa:", None))
        self.Zapisz_wynik.setText(QCoreApplication.translate("MainWindow", u"Zapisz wyniki", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Wyniki wzorcowania:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Swiadectwo), QCoreApplication.translate("MainWindow", u"Swiadectwo", None))
        self.label_8.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program do wzorcowania multimetr\u00f3w.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sprz\u0119t: Kalibrator 5100B (GPIB)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Autor: Mateusz Witas</p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">email: matekw26@gmail.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Instrukcja (mo\u017ce jaka\u015b)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Przycisk reset: Troch\u0119 funkcja STOP, pocz\u0105tkowe ustawienia kalibratora jak i arkuszy...</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Przycisk help: Kalibrator na zdalny, wybierz model lub ustaw zakres, odpowiednie pod\u0142\u0105czenie...</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Informacje), QCoreApplication.translate("MainWindow", u"Informacje", None))
    # retranslateUi

