import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog, QMessageBox
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QCloseEvent
from MainWindowui import Ui_MainWindow
# from docx import Document
# from docx.shared import Inches
import os
import subprocess
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import Border, Side, Font, PatternFill, colors
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule, FormulaRule
from openpyxl import Workbook


# 1 instalacja PySide6 ... pip install PySide6?
# 2 instalacja docx do Worda pip install python-docx... nie przyda sie chyba
# 3 aktualizacja gui pyside6-uic mainwindow.ui -o MainWindowui.py
# 4 instalacja Excela pip install openpyxl
# 5 Import obrazu do excela pip install Pillow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # cos do zapisu
        self.initUI()

        # aktualna data do SW
        self.data_wzorcowania.setDate(QDate.currentDate())

        # guziki do kalibratora
        self.wartosc_kalibrator.valueChanged.connect(self.odczytaj)
        self.Nastaw.clicked.connect(self.nastawa)
        self.Wyczysc.clicked.connect(self.wyczysc)
        # odczyt wartośći z listy AC/DC
        self.AC_DC.currentTextChanged.connect(self.text_changed)

        # usunąc potem
        self.AC_DC.currentTextChanged.connect(self.odczytaj)

        # odczyt wartości z listy mV/V/mA/A
        self.ustawienie_kalibrator.currentTextChanged.connect(self.text_changed)

        # usunąc potem
        self.ustawienie_kalibrator.currentTextChanged.connect(self.odczytaj)

        # podanie sciezki zapisu
        self.sciezkaSW_zapis.setText(u"Zapis_Swiadectw_Wzorcowania/nazwa_pliku")
        self.sciezkaWynik_zapis.setText(u"Zapis_Wynikow_Wzorcowania/nazwa_pliku")

        # odczyt wynikow
        self.odczyt_wynikow.clicked.connect(self.open_file_dialog)

        # szukaj plikow
        self.SzukajWynikow.clicked.connect(self.save_file_dialog)
        self.SzukajSW.clicked.connect(self.save_file_dialog)

        # zamkniecie aplikacji
        self.zamkniecie_aplikacji.clicked.connect(QApplication.instance().quit)

        # wybor zglaszajacego
        self.Wybor_zglaszajacy.currentTextChanged.connect(self.zglaszajacy)

        # generowanie swiadectwa
        self.generuj_swiadectwo.clicked.connect(self.swiadectwo)





    def zglaszajacy(self):
        print(self.Wybor_zglaszajacy.currentText())
        if self.Wybor_zglaszajacy.currentText() == "Linetech":
            lt = "LINETECH S.A. \nul. Warecka 11A \n00-034 Warszawa"
            self.Zglaszajacy.setText(lt)
        elif self.Wybor_zglaszajacy.currentText() == "Hitachi":
            hitachi = "Hitachi Energy Poland Sp. z o.o. \nul. Leszno 59 \n06-300 Przasnysz"
            self.Zglaszajacy.setText(hitachi)
        elif self.Wybor_zglaszajacy.currentText() == "Hanza":
            hanza = "HANZA POLAND SP.Z O.O. \nAL.JEROZOLIMSKIE 38 \n56 - 120 BRZEG DOLNY"
            self.Zglaszajacy.setText(hanza)


    def text_changed(self, s):  # s is a str
        print(s)

    def nastawa(self):
        print(f'Ustawiona wartosc kalibratora to: ', self.wartosc_kalibrator.value(),
              self.ustawienie_kalibrator.currentText(), self.AC_DC.currentText())

    def odczytaj(self):
        print("Ustawiona wartosc kalibratora:", self.wartosc_kalibrator.value())
        self.odczyt_kalibrator.setText(str(self.wartosc_kalibrator.value()) + " " +
                                       str(self.ustawienie_kalibrator.currentText()) + " " +
                                       str(self.AC_DC.currentText()))

    def wyczysc(self):
        self.wartosc_kalibrator.setValue(0)

    # funkcja do otwierania folderu
    def open_folder(self, file_path):
        folder_path = os.path.dirname(file_path)  # uzyskanie ścieżki do folderu
        os.startfile(folder_path)  # otwarcie folderu w eksploratorze plików

    # funkcja do otwierania okna dialogowego
    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Otwórz plik", "",
                                                   "All Files (*);;Excel Files (*.xlsx)", options=options)
        if file_name:
            sender = self.sender()
            # tutaj ustawiam ścieżkę na QLineEdit
            if sender.objectName() == "SzukajSW":
                path = file_name
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezkaSW_zapis.setText(filename_without_ext)
                print(file_name)
            elif sender.objectName() == "SzukajWynikow":
                path = file_name
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezkaWynik_zapis.setText(filename_without_ext)
                print(file_name)


    # funkcja do zapisu
    def save_file_dialog(self):
        options = QFileDialog.Options()
        self.saveFileDialog.setDirectory(self.sciezkaSW_zapis.text())
        fileName, _ = self.saveFileDialog.getSaveFileName(self, "Save File",
                                                          self.sciezkaSW_zapis.text(),
                                                          "Excel Files (*.xlsx);;All Files (*)",
                                                          options=options)
        if fileName:
            sender = self.sender()
            # tutaj ustawiam ścieżkę na QLineEdit
            if sender.objectName() == "SzukajSW":
                path = fileName
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezkaSW_zapis.setText(filename_without_ext)
                print(fileName)
            elif sender.objectName() == "SzukajWynikow":
                path = fileName
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezkaWynik_zapis.setText(filename_without_ext)
                print(fileName)
            # Zapisz plik w wybranej ścieżce
            with open(fileName, 'w') as f:
                f.write("Tutaj jest tekst, który zostanie zapisany w pliku.")

    # cos do zapisu
    def initUI(self):
        # ...
        self.saveFileDialog = QFileDialog()
        self.saveFileDialog.setAcceptMode(QFileDialog.AcceptSave)
        self.saveFileDialog.setFileMode(QFileDialog.AnyFile)
        self.saveFileDialog.setNameFilter("Excel Files (*.xlsx)")


    # zamkniecie aplikacji
    def closeEvent(self, event: QCloseEvent):
        czy_zamknac = QMessageBox.question(self, "Zamknąć aplikacje?", "Czy na pewno chcesz wyjśc z programu?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if czy_zamknac == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


    # generowanie świadectwa
    def swiadectwo(self):

        # # Ustawienie wartości w komórce
        # worksheet.cell(row=1, column=1, value="Hello World!")

        # Tworzenie nowego pliku Excel
        wb = Workbook()
        # Tworzenie nowego arkusza
        ws = wb.active

        # Połączenie komórek
        for row in range(7, 15):
            ws.merge_cells(f"C{row}:E{row}")

        for col in ['B', 'C', 'D', 'E']:
            ws.merge_cells(f'{col}4:{col}5')

        ws.merge_cells("C2:E2")
        ws.merge_cells("B3:E3")
        ws.merge_cells("B15:E19")
        # ws.merge_cells("A4:D5")

        # ustawianie stylu obramowania dla komórek
        border_style = Side(border_style='thin', color='000000')
        border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)

        # ustawienie obramowania dla komórki
        for row in range(2, 20):
            if row != 6:
                for column in range(2, 6):
                    cell = ws.cell(row=row, column=column)
                    cell.border = border

        # ustawienie wielkośći komórek
        ws.row_dimensions[2].height = 90
        ws.row_dimensions[3].height = 41.25
        ws.row_dimensions[4].height = 15
        ws.row_dimensions[5].height = 15
        ws.row_dimensions[6].height = 15
        ws.row_dimensions[7].height = 53.25
        ws.row_dimensions[8].height = 45.75
        ws.row_dimensions[9].height = 37.50
        ws.row_dimensions[10].height = 48
        ws.row_dimensions[11].height = 37.50
        ws.row_dimensions[12].height = 79.50
        ws.row_dimensions[13].height = 108.75
        ws.row_dimensions[14].height = 37.50
        ws.row_dimensions[19].height = 21

        ws.column_dimensions['A'].width = 1
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 13.71
        ws.column_dimensions['D'].width = 30.57
        ws.column_dimensions['E'].width = 20.85

        # ustawianie czcionki i pozycji tekstu
        alignmentCT = Alignment(wrap_text=True, horizontal='center', vertical='top')
        alignmentCC = Alignment(wrap_text=True, horizontal='center', vertical='center')
        alignmentLC = Alignment(wrap_text=True, horizontal='left', vertical='center')
        alignmentLT = Alignment(wrap_text=True, horizontal='left', vertical='top')
        fontA12 = Font(name='Arial', size=12)
        fontA22 = Font(name='Arial', size=22)
        fontA10 = Font(name='Arial', size=10)
        fontA10B = Font(name='Arial', size=10, bold=True)

        # wstawienie loga
        img = Image('image/logov3.png')
        img.height = 116
        img.width = 140
        ws.add_image(img, 'B2')

        ws['C2'] = ('Metro-Lab Agnieszka Greń \n '
                    'Warszawa 01-386 ul. Reżyserska 5 \n '
                    'tel. (+48) 661 472 870 \n '
                    'e-mail: poczta@metro-lab.pl \n'
                    'www.metro-lab.pl')

        ws['C2'].alignment = alignmentCC
        ws['C2'].font = fontA12

        ws['B3'] = "ŚWIADECTWO WZORCOWANIA ESSA"
        ws['B3'].font = fontA22
        ws['B3'].alignment = alignmentCC

        ws['B4'] = "Data wydania:"
        ws['B4'].font = fontA10
        ws['B4'].alignment = alignmentLC

        ws['C4'] = self.data_wzorcowania.text()
        ws['C4'].font = fontA10
        ws['C4'].alignment = alignmentLC

        ws['D4'] = "Nr świadectwa: " + self.numer_swiadectwa.text()
        ws['D4'].font = fontA10
        ws['D4'].alignment = alignmentLC

        ws['E4'] = "Strona 1/6" #ogarnac str
        ws['E4'].font = fontA10
        ws['E4'].alignment = alignmentLC

        ws['B7'] = "PRZEDMIOT \nWZORCOWANIA"
        ws['B8'] = "ZGŁASZAJĄCY"
        ws['B9'] = "METODA \nWZORCOWANIA"
        ws['B10'] = "WARUNKI \nŚRODOWISKOWE"
        ws['B11'] = "DATA WYKONANIA \nWZORCOWANIA"
        ws['B12'] = "SPÓJNOŚĆ \nPOMIAROWA"
        ws['B13'] = "NIEPEWNOŚĆ \nPOMIARU"
        ws['B14'] = "WYNIKI \nWZOROCWANIA"

        ws['C7'] = self.przedmiot_wzorcowania.toPlainText()
        ws['C8'] = self.Zglaszajacy.toPlainText()
        ws['C9'] = self.metoda_wzorcowania.toPlainText()
        ws['C10'] = self.warunki_srodowiskowe.toPlainText()
        ws['C11'] = self.data_wzorcowania.text()
        ws['C12'] = self.spojnosc_pomiarowa.toPlainText()
        ws['C13'] = self.niepewnosc_pomiaru.toPlainText()
        ws['C14'] = "Podano na kolejnych stronach niniejszego świadectwa"
        ws['B15'] = "                                               Robert Greń"



        # iteracja po wierszach i kolumnach, zmiana stylu komórek
        for row in range(6, 20):
                cell = ws.cell(row=row, column=3)
                cell.font = fontA10
                cell.alignment = alignmentLC

        for row in range(6, 20):
                cell = ws.cell(row=row, column=2)
                cell.font = fontA10B
                cell.alignment = alignmentLC

        # ws['C7'].alignment = alignmentLC
        # ws['C10'].alignment = alignmentLC
        # ws['C11'].alignment = alignmentLC
        ws['B15'].alignment = alignmentCC
        ws['B15'].font = fontA10

        # Zapisanie pliku
        if os.path.exists(self.sciezkaSW_zapis.text() + ".xlsx"):
            # Wyświetlenie okna dialogowego z pytaniem o nadpisanie pliku
            msg_box = QMessageBox()
            msg_box.setText("Plik już istnieje. Czy chcesz go nadpisać?")
            msg_box.setWindowTitle("Nadpisać plik?")
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            # Obsługa wyboru użytkownika
            choice = msg_box.exec()
            if choice == QMessageBox.Yes:
                try:
                    os.remove(self.sciezkaSW_zapis.text() + ".xlsx")
                    print("Plik już istnieje, nadpisywanie...")
                    wb.save(self.sciezkaSW_zapis.text() + ".xlsx")
                    self.open_folder(self.sciezkaSW_zapis.text())
                except PermissionError as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Błąd zapisu pliku")
                    msg.setInformativeText(str(e))
                    msg.setWindowTitle("Błąd")
                    msg.exec()
        else:
            print("Plik nie istnieje, zapisywanie...")
            wb.save(self.sciezkaSW_zapis.text() + ".xlsx")
            self.open_folder(self.sciezkaSW_zapis.text())




app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()



