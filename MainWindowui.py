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

        self.Reset = QPushButton(self.Pomiary)
        self.Reset.setObjectName(u"Reset")

        self.gridLayout.addWidget(self.Reset, 6, 27, 1, 2)

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

        self.Tabwybor = QTabWidget(self.Pomiary)
        self.Tabwybor.setObjectName(u"Tabwybor")
        self.DCV = QWidget()
        self.DCV.setObjectName(u"DCV")
        self.gridLayout_2 = QGridLayout(self.DCV)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ZapiszDCV = QPushButton(self.DCV)
        self.ZapiszDCV.setObjectName(u"ZapiszDCV")

        self.gridLayout_2.addWidget(self.ZapiszDCV, 6, 5, 1, 1)

        self.podlaczenieDCV = QLabel(self.DCV)
        self.podlaczenieDCV.setObjectName(u"podlaczenieDCV")
        self.podlaczenieDCV.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.podlaczenieDCV.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.podlaczenieDCV, 2, 5, 1, 1)

        self.NextDCV = QPushButton(self.DCV)
        self.NextDCV.setObjectName(u"NextDCV")

        self.gridLayout_2.addWidget(self.NextDCV, 5, 5, 1, 1)

        self.PomiarDCV = QPushButton(self.DCV)
        self.PomiarDCV.setObjectName(u"PomiarDCV")

        self.gridLayout_2.addWidget(self.PomiarDCV, 4, 5, 1, 1)

        self.wynikiDCV = QTableWidget(self.DCV)
        self.wynikiDCV.setObjectName(u"wynikiDCV")

        self.gridLayout_2.addWidget(self.wynikiDCV, 0, 0, 8, 1)

        self.KasujDCV = QPushButton(self.DCV)
        self.KasujDCV.setObjectName(u"KasujDCV")

        self.gridLayout_2.addWidget(self.KasujDCV, 7, 5, 1, 1)

        self.Tabwybor.addTab(self.DCV, "")
        self.ACV = QWidget()
        self.ACV.setObjectName(u"ACV")
        self.gridLayout_3 = QGridLayout(self.ACV)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.KasujACV = QPushButton(self.ACV)
        self.KasujACV.setObjectName(u"KasujACV")

        self.gridLayout_3.addWidget(self.KasujACV, 7, 5, 1, 1)

        self.wynikiACV = QTableWidget(self.ACV)
        self.wynikiACV.setObjectName(u"wynikiACV")

        self.gridLayout_3.addWidget(self.wynikiACV, 0, 1, 8, 1)

        self.ZapiszACV = QPushButton(self.ACV)
        self.ZapiszACV.setObjectName(u"ZapiszACV")

        self.gridLayout_3.addWidget(self.ZapiszACV, 6, 5, 1, 1)

        self.NextACV = QPushButton(self.ACV)
        self.NextACV.setObjectName(u"NextACV")

        self.gridLayout_3.addWidget(self.NextACV, 5, 5, 1, 1)

        self.PomiarACV = QPushButton(self.ACV)
        self.PomiarACV.setObjectName(u"PomiarACV")

        self.gridLayout_3.addWidget(self.PomiarACV, 4, 5, 1, 1)

        self.PodlaczenieACV = QLabel(self.ACV)
        self.PodlaczenieACV.setObjectName(u"PodlaczenieACV")
        self.PodlaczenieACV.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.PodlaczenieACV.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.PodlaczenieACV, 2, 5, 1, 1)

        self.Tabwybor.addTab(self.ACV, "")
        self.DCI = QWidget()
        self.DCI.setObjectName(u"DCI")
        self.gridLayout_4 = QGridLayout(self.DCI)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.PodlaczenieDCI = QLabel(self.DCI)
        self.PodlaczenieDCI.setObjectName(u"PodlaczenieDCI")
        self.PodlaczenieDCI.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.PodlaczenieDCI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.PodlaczenieDCI, 0, 2, 1, 2)

        self.wynikiDCI = QTableWidget(self.DCI)
        self.wynikiDCI.setObjectName(u"wynikiDCI")

        self.gridLayout_4.addWidget(self.wynikiDCI, 0, 1, 5, 1)

        self.PomiarDCI = QPushButton(self.DCI)
        self.PomiarDCI.setObjectName(u"PomiarDCI")

        self.gridLayout_4.addWidget(self.PomiarDCI, 1, 2, 1, 2)

        self.NextDCI = QPushButton(self.DCI)
        self.NextDCI.setObjectName(u"NextDCI")

        self.gridLayout_4.addWidget(self.NextDCI, 2, 2, 1, 2)

        self.ZapiszDCI = QPushButton(self.DCI)
        self.ZapiszDCI.setObjectName(u"ZapiszDCI")

        self.gridLayout_4.addWidget(self.ZapiszDCI, 3, 2, 1, 2)

        self.KasujDCI = QPushButton(self.DCI)
        self.KasujDCI.setObjectName(u"KasujDCI")

        self.gridLayout_4.addWidget(self.KasujDCI, 4, 2, 1, 2)

        self.Tabwybor.addTab(self.DCI, "")
        self.ACI = QWidget()
        self.ACI.setObjectName(u"ACI")
        self.gridLayout_5 = QGridLayout(self.ACI)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.PodlaczenieACI = QLabel(self.ACI)
        self.PodlaczenieACI.setObjectName(u"PodlaczenieACI")
        self.PodlaczenieACI.setPixmap(QPixmap(u"image/polaczenieUIv444.png"))
        self.PodlaczenieACI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.PodlaczenieACI, 0, 2, 1, 2)

        self.wynikiACI = QTableWidget(self.ACI)
        self.wynikiACI.setObjectName(u"wynikiACI")

        self.gridLayout_5.addWidget(self.wynikiACI, 0, 1, 5, 1)

        self.PomiarACI = QPushButton(self.ACI)
        self.PomiarACI.setObjectName(u"PomiarACI")

        self.gridLayout_5.addWidget(self.PomiarACI, 1, 2, 1, 2)

        self.NextACI = QPushButton(self.ACI)
        self.NextACI.setObjectName(u"NextACI")

        self.gridLayout_5.addWidget(self.NextACI, 2, 2, 1, 2)

        self.ZapiszACI = QPushButton(self.ACI)
        self.ZapiszACI.setObjectName(u"ZapiszACI")

        self.gridLayout_5.addWidget(self.ZapiszACI, 3, 2, 1, 2)

        self.KasujACI = QPushButton(self.ACI)
        self.KasujACI.setObjectName(u"KasujACI")

        self.gridLayout_5.addWidget(self.KasujACI, 4, 2, 1, 2)

        self.Tabwybor.addTab(self.ACI, "")
        self.R = QWidget()
        self.R.setObjectName(u"R")
        self.gridLayout_6 = QGridLayout(self.R)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.KasujR = QPushButton(self.R)
        self.KasujR.setObjectName(u"KasujR")
        self.KasujR.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.KasujR, 1, 2, 1, 1)

        self.ZapiszR = QPushButton(self.R)
        self.ZapiszR.setObjectName(u"ZapiszR")
        self.ZapiszR.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.ZapiszR, 1, 1, 1, 1)

        self.wynikiR = QTableWidget(self.R)
        self.wynikiR.setObjectName(u"wynikiR")

        self.gridLayout_6.addWidget(self.wynikiR, 0, 0, 1, 3)

        self.Tabwybor.addTab(self.R, "")

        self.gridLayout.addWidget(self.Tabwybor, 5, 0, 1, 32)

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
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.addItem("")
        self.ustawienie_kalibrator.setObjectName(u"ustawienie_kalibrator")

        self.gridLayout.addWidget(self.ustawienie_kalibrator, 6, 2, 1, 2)

        self.wybierz_model = QComboBox(self.Pomiary)
        self.wybierz_model.setObjectName(u"wybierz_model")

        self.gridLayout.addWidget(self.wybierz_model, 1, 1, 1, 2)

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

        self.zakresACV_2 = QDoubleSpinBox(self.Pomiary)
        self.zakresACV_2.setObjectName(u"zakresACV_2")
        self.zakresACV_2.setMaximumSize(QSize(60, 16777210))
        self.zakresACV_2.setMaximum(1000.000000000000000)
        self.zakresACV_2.setValue(400.000000000000000)

        self.gridLayout.addWidget(self.zakresACV_2, 2, 17, 1, 1)

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
        self.data_wzorcowania.setDateTime(QDateTime(QDate(2023, 2, 9), QTime(11, 0, 0)))
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
        self.Komunikacja = QWidget()
        self.Komunikacja.setObjectName(u"Komunikacja")
        self.label_3 = QLabel(self.Komunikacja)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 1488, 110))
        self.label_3.setPixmap(QPixmap(u"image/tlo_poloficial.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.Komunikacja)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 91, 21))
        self.label_5 = QLabel(self.Komunikacja)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 91, 16))
        self.kalibrator_adres = QComboBox(self.Komunikacja)
        self.kalibrator_adres.addItem("")
        self.kalibrator_adres.setObjectName(u"kalibrator_adres")
        self.kalibrator_adres.setGeometry(QRect(20, 160, 161, 24))
        self.multimetr_adres = QComboBox(self.Komunikacja)
        self.multimetr_adres.addItem("")
        self.multimetr_adres.setObjectName(u"multimetr_adres")
        self.multimetr_adres.setGeometry(QRect(20, 210, 161, 24))
        self.status_kal = QLineEdit(self.Komunikacja)
        self.status_kal.setObjectName(u"status_kal")
        self.status_kal.setGeometry(QRect(340, 160, 571, 24))
        self.label_16 = QLabel(self.Komunikacja)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(340, 140, 81, 16))
        self.status_dmm = QLineEdit(self.Komunikacja)
        self.status_dmm.setObjectName(u"status_dmm")
        self.status_dmm.setGeometry(QRect(340, 210, 571, 24))
        self.label_18 = QLabel(self.Komunikacja)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(340, 190, 81, 16))
        self.polacz_kal = QPushButton(self.Komunikacja)
        self.polacz_kal.setObjectName(u"polacz_kal")
        self.polacz_kal.setGeometry(QRect(250, 160, 80, 24))
        self.polacz_dmm = QPushButton(self.Komunikacja)
        self.polacz_dmm.setObjectName(u"polacz_dmm")
        self.polacz_dmm.setGeometry(QRect(250, 210, 80, 24))
        self.odswiez = QPushButton(self.Komunikacja)
        self.odswiez.setObjectName(u"odswiez")
        self.odswiez.setGeometry(QRect(190, 160, 51, 21))
        self.label_19 = QLabel(self.Komunikacja)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 250, 81, 16))
        self.error1 = QLineEdit(self.Komunikacja)
        self.error1.setObjectName(u"error1")
        self.error1.setGeometry(QRect(20, 280, 461, 24))
        self.error2 = QLineEdit(self.Komunikacja)
        self.error2.setObjectName(u"error2")
        self.error2.setGeometry(QRect(20, 310, 461, 24))
        self.error3 = QLineEdit(self.Komunikacja)
        self.error3.setObjectName(u"error3")
        self.error3.setGeometry(QRect(20, 340, 461, 24))
        self.tabWidget.addTab(self.Komunikacja, "")
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

        self.tabWidget.setCurrentIndex(2)
        self.Tabwybor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiMeasure", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Odczytana warto\u015b\u0107:", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Wyczysc.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107", None))
        self.ZapiszDCV.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.podlaczenieDCV.setText("")
        self.NextDCV.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.PomiarDCV.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.KasujDCV.setText(QCoreApplication.translate("MainWindow", u"Odblokuj", None))
        self.Tabwybor.setTabText(self.Tabwybor.indexOf(self.DCV), QCoreApplication.translate("MainWindow", u"DCV", None))
        self.KasujACV.setText(QCoreApplication.translate("MainWindow", u"Odblokuj", None))
        self.ZapiszACV.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.NextACV.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.PomiarACV.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.PodlaczenieACV.setText("")
        self.Tabwybor.setTabText(self.Tabwybor.indexOf(self.ACV), QCoreApplication.translate("MainWindow", u"ACV", None))
        self.PodlaczenieDCI.setText("")
        self.PomiarDCI.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.NextDCI.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ZapiszDCI.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.KasujDCI.setText(QCoreApplication.translate("MainWindow", u"Odblokuj", None))
        self.Tabwybor.setTabText(self.Tabwybor.indexOf(self.DCI), QCoreApplication.translate("MainWindow", u"DCI", None))
        self.PodlaczenieACI.setText("")
        self.PomiarACI.setText(QCoreApplication.translate("MainWindow", u"POMIAR", None))
        self.NextACI.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ZapiszACI.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.KasujACI.setText(QCoreApplication.translate("MainWindow", u"Odblokuj", None))
        self.Tabwybor.setTabText(self.Tabwybor.indexOf(self.ACI), QCoreApplication.translate("MainWindow", u"ACI", None))
        self.KasujR.setText(QCoreApplication.translate("MainWindow", u"Kasuj Wyniki", None))
        self.ZapiszR.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.Tabwybor.setTabText(self.Tabwybor.indexOf(self.R), QCoreApplication.translate("MainWindow", u"R", None))
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
        self.ustawienie_kalibrator.setItemText(0, QCoreApplication.translate("MainWindow", u"uV", None))
        self.ustawienie_kalibrator.setItemText(1, QCoreApplication.translate("MainWindow", u"mV", None))
        self.ustawienie_kalibrator.setItemText(2, QCoreApplication.translate("MainWindow", u"V", None))
        self.ustawienie_kalibrator.setItemText(3, QCoreApplication.translate("MainWindow", u"uA", None))
        self.ustawienie_kalibrator.setItemText(4, QCoreApplication.translate("MainWindow", u"mA", None))
        self.ustawienie_kalibrator.setItemText(5, QCoreApplication.translate("MainWindow", u"A", None))

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
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Kalibrator adres", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Multimetr adres", None))
        self.kalibrator_adres.setItemText(0, QCoreApplication.translate("MainWindow", u"GPIB0::7::INSTR", None))

        self.multimetr_adres.setItemText(0, QCoreApplication.translate("MainWindow", u"GPIB0::1::INSTR", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.polacz_kal.setText(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz", None))
        self.polacz_dmm.setText(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz", None))
        self.odswiez.setText(QCoreApplication.translate("MainWindow", u"Od\u015bwie\u017c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Komunikaty:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Komunikacja), QCoreApplication.translate("MainWindow", u"Komunikacja", None))
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

