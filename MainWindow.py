import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QCloseEvent, QPen, QColor, QStandardItem, QStandardItemModel
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
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
import numpy as np
import xlsxwriter


# 1 instalacja PySide6 ... pip install PySide6
# 2 instalacja docx do Worda pip install python-docx... nie przyda sie chyba
# 3 aktualizacja gui pyside6-uic mainwindow.ui -o MainWindowui.py
# 4 instalacja Excela pip install openpyxl
# 5 Import obrazu do excela pip install Pillow
# 6 generowanie excela pip install xlsxwriter

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
        self.sciezkaWynik_zapis.setText(u"Zapis_Wynikow_Wzorcowania/Przyklad")
        self.sciezka_Model.setText(u"Modele/tescik")


        # odczyt wynikow
        self.odczyt_wynikow.clicked.connect(self.open_file_dialog)
        # self.odczyt_wynikow.clicked.connect(self.loadExcelData2(self.sciezkaWynik_zapis.text() + ".xlsx", self.wyniki_wzorcowania))

        self.SzukajModelu.clicked.connect(self.open_file_dialog)
        # self.SzukajModelu.clicked.connect(self.loadExcelData2(self.sciezkaModel.text() + ".xlsx" + self.wynikiDCV))

        # szukaj plikow
        self.SzukajWynikow.clicked.connect(self.save_file_dialog)
        self.SzukajSW.clicked.connect(self.save_file_dialog)


        # zamkniecie aplikacji
        self.zamkniecie_aplikacji.clicked.connect(QApplication.instance().quit)

        # wybor zglaszajacego
        self.Wybor_zglaszajacy.currentTextChanged.connect(self.zglaszajacy)

        # generowanie swiadectwa
        self.generuj_swiadectwo.clicked.connect(self.swiadectwo)

        # zapisywanie wynikow
        self.Zapisz_wynik.clicked.connect(self.save_to_excel)

        # Tworzenie excela
        self.Stworz.clicked.connect(self.generate_excel)

        # update tabeli
        # self.loadExcelData()
        # self.loadExcelData2(self.sciezkaWynik_zapis.text() +".xlsx", self.wyniki_wzorcowania)




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
            elif sender.objectName() == "SzukajModelu":
                path = file_name
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezka_Model.setText(filename_without_ext)
                self.loadExcelData2(self.sciezka_Model.text() + ".xlsx", self.wynikiDCV)
                print(file_name)
            elif sender.objectName() == "SzukajWynikow" or "odczyt_wynikow":
                path = file_name
                filename_without_ext, ext = os.path.splitext(path)
                self.sciezkaWynik_zapis.setText(filename_without_ext)
                self.loadExcelData2(self.sciezkaWynik_zapis.text() + ".xlsx", self.wyniki_wzorcowania)
                print(file_name)


    # def loadExcelData(self):
    #     path = self.sciezkaWynik_zapis.text() +".xlsx"
    #     df = pd.read_excel(path)
    #     if df.size == 0:
    #         return
    #
    #     df.fillna('', inplace=True)
    #     self.wyniki_wzorcowania.setRowCount(df.shape[0])
    #     self.wyniki_wzorcowania.setColumnCount(df.shape[1])
    #     column_headers = df.iloc[3]
    #     self.wyniki_wzorcowania.setHorizontalHeaderLabels(column_headers)
    #
    #     # ustawienie dopasowywania się rozmiaru kolumn
    #     for i in range(self.wyniki_wzorcowania.columnCount()):
    #          self.wyniki_wzorcowania.resizeColumnToContents(i)
    #
    #     # Wyświetlanie danych z Excela
    #     for row in df.iterrows():
    #         values = row[1]
    #         for col_index, value in enumerate(values):
    #             tableItem = QTableWidgetItem(str(value))
    #             self.wyniki_wzorcowania.setItem(row[0], col_index, tableItem)
    #
    #     # Ustawienie poprakwi kolumn 2 i 3 w kolumnie 4
    #     self.wyniki_wzorcowania.itemChanged.connect(self.update_tablewidget)
    #
    #     # self.update_tablewidget()
    #     self.wyniki_wzorcowania.setStyleSheet("QTableView::item { border: 0px solid black; }")

    def loadExcelData2(self, path, table):
        df = pd.read_excel(path)
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        column_headers = df.iloc[3]
        table.setHorizontalHeaderLabels(column_headers)

        # ustawienie dopasowywania się rozmiaru kolumn
        for i in range(table.columnCount()):
             table.resizeColumnToContents(i)

        # Wyświetlanie danych z Excela
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                tableItem = QTableWidgetItem(str(value))
                table.setItem(row[0], col_index, tableItem)

        # Ustawienie poprakwi kolumn 2 i 3 w kolumnie 4
        table.itemChanged.connect(lambda item: self.update_tablewidget(item, table2=table))

        # self.update_tablewidget()
        table.setStyleSheet("QTableView::item { border: 0px solid black; }")

    def update_tablewidget(self, item, table2):
        # Obliczanie poprakwi
        row = item.row()
        col = item.column()
        try:
            if col == 2 or col == 3:
                value1 = float(table2.item(row, 2).text())
                value2 = float(table2.item(row, 3).text())
                result = np.around(value1 - value2, decimals=5)
                table2.item(row, 4).setText(str(result))
        except ValueError:
            pass
        except AttributeError:
            pass

        # for row in range(self.wyniki_wzorcowania.rowCount()):
        #     try:
        #         item1 = self.wyniki_wzorcowania.item(row, 2)
        #         item2 = self.wyniki_wzorcowania.item(row, 3)
        #         if item1.text() or item2.text() != "":
        #             value_1 = float(self.wyniki_wzorcowania.item(row, 2).text())
        #             value_2 = float(self.wyniki_wzorcowania.item(row, 3).text())
        #             result = value_1 + value_2
        #             item = QTableWidgetItem()
        #             item.setData(Qt.EditRole, result)
        #             self.wyniki_wzorcowania.setItem(row, 4, item)
        #     except ValueError:
        #         pass

    def save_to_excel(self):

        # Tworzenie nowego arkusza w pliku Excel
        wb = openpyxl.Workbook()
        ws = wb.active

        # ustawianie stylu obramowania dla komórek
        border_style = Side(border_style='thin', color='000000')
        border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)

        alignmentCC = Alignment(wrap_text=True, horizontal='center', vertical='center')


        # Pobieranie danych z QTableWidget i zapisywanie ich do arkusza
        for row in range(self.wyniki_wzorcowania.rowCount()):
            for col in range(self.wyniki_wzorcowania.columnCount()):
                item = self.wyniki_wzorcowania.item(row, col)
                if item is not None:
                    ws.cell(row=row + 2, column=col + 1, value=item.text())

        # # ustawienie obramowania dla komórki
        # for row in range(self.wyniki_wzorcowania.rowCount()):
        #     for col in range(self.wyniki_wzorcowania.columnCount()):
        #         item = self.wyniki_wzorcowania.item(row, col)
        #         # print(item.text())
        #         if item.text() != "":
        #             cell = ws.cell(row=row + 2, column=col + 1)
        #             cell.border = border
        #             cell.alignment = Alignment(wrapText=True)
        #             cell.alignment = alignmentCC
        #
        #
        # # Dopasowanie szerokości kolumn do zawartości
        # for col in range(self.wyniki_wzorcowania.columnCount()):
        #     column_letter = get_column_letter(col + 1)
        #     column_dimensions = ws.column_dimensions[column_letter]
        #     max_length = 0
        #     for cell in ws[column_letter]:
        #         try:
        #             cell_value = str(cell.value)
        #         except:
        #             cell_value = ""
        #         if len(cell_value) > max_length:
        #             max_length = len(cell_value)
        #             print(max_length)
        #     if max_length < 30:
        #         adjusted_width = (max_length + 2)
        #         column_dimensions.width = adjusted_width

        # ustawienie obramowania dla komórki i dopasowanie szerokosci kolumn
        for row in range(self.wyniki_wzorcowania.rowCount()):
            for col in range(self.wyniki_wzorcowania.columnCount()):
                column_letter = get_column_letter(col + 1)
                column_dimensions = ws.column_dimensions[column_letter]
                max_length = 0
                for cell in ws[column_letter]:
                    try:
                        cell_value = str(cell.value)
                    except:
                        cell_value = ""
                    if len(cell_value) > max_length:
                        max_length = len(cell_value)
                        # print(max_length)
                if max_length < 30:
                    adjusted_width = (max_length + 2)
                    column_dimensions.width = adjusted_width
                item = self.wyniki_wzorcowania.item(row, col)
                 # print(item.text())
                if item.text() != "":
                    cell1 = ws.cell(row=row + 2, column=col + 1)
                    cell1.border = border
                    cell1.alignment = Alignment(wrapText=True)
                    cell1.alignment = alignmentCC

        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 13
        ws.column_dimensions['F'].width = 14


        self.zapis_pliku(self.sciezkaWynik_zapis.text(), wb)

    # def saveadd_to_excel(self):
    #
    #     # Otwieranie arkusza w pliku Excel
    #     wb = openpyxl.load_workbook('nazwa_pliku.xlsx')
    #     ws = wb['Sheet']
    #
    #     # ustawianie stylu obramowania dla komórek
    #     border_style = Side(border_style='thin', color='000000')
    #     border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)
    #
    #     alignmentCC = Alignment(wrap_text=True, horizontal='center', vertical='center')
    #
    #     # Pobieranie danych z QTableWidget i zapisywanie ich do arkusza
    #     for row in range(self.wyniki_wzorcowania.rowCount()):
    #         for col in range(self.wyniki_wzorcowania.columnCount()):
    #             item = self.wyniki_wzorcowania.item(row, col)
    #             if item is not None:
    #                 ws.cell(row=row + 32, column=col + 31, value=item.text())
    #
    #
    #     # ustawienie obramowania dla komórki i dopasowanie szerokosci kolumn
    #     for row in range(self.wyniki_wzorcowania.rowCount()):
    #         for col in range(self.wyniki_wzorcowania.columnCount()):
    #             column_letter = get_column_letter(col + 1)
    #             column_dimensions = ws.column_dimensions[column_letter]
    #             max_length = 0
    #             for cell in ws[column_letter]:
    #                 try:
    #                     cell_value = str(cell.value)
    #                 except:
    #                     cell_value = ""
    #                 if len(cell_value) > max_length:
    #                     max_length = len(cell_value)
    #                     # print(max_length)
    #             if max_length < 30:
    #                 adjusted_width = (max_length + 2)
    #                 column_dimensions.width = adjusted_width
    #             item = self.wyniki_wzorcowania.item(row, col)
    #              # print(item.text())
    #             if item.text() != "":
    #                 cell1 = ws.cell(row=row + 2, column=col + 1)
    #                 cell1.border = border
    #                 cell1.alignment = Alignment(wrapText=True)
    #                 cell1.alignment = alignmentCC
    #
    #     ws.column_dimensions['C'].width = 12
    #     ws.column_dimensions['D'].width = 13
    #     ws.column_dimensions['F'].width = 14
    #
    #     self.zapis_pliku(self.sciezkaWynik_zapis.text(), wb)

    def generate_excel(self):

        wb = Workbook()
        ws = wb.active

        col_headers = ['Zakres', 'Wartość napięcia odniesienia',
                       'Zmierzona wartość napięcia', 'Poprawka', 'Niepewność pomiaru']
        row_headers = ['mV', str(float(self.zakresDCV_2.value())), '', '', '', 'V',
                       str(float(self.zakresDCV_2.value())/100), '', '', '',
                       str(float(self.zakresDCV_2.value())/10), '', '', '',
                       str(self.zakresDCV_2.value()), '', '', '',
                       str(self.zakresDCV.text()), '', '', '']

        # ustawianie stylu obramowania dla komórek
        border_style = Side(border_style='thin', color='000000')
        border = Border(left=border_style, right=border_style, top=border_style, bottom=border_style)

        # ustawianie czcionki i pozycji tekstu
        alignmentCC = Alignment(wrap_text=True, horizontal='center', vertical='center')
        fontA10 = Font(name='Arial', size=10)

        if self.check_dcv.isChecked():
            for i, col in enumerate(col_headers):
                ws.cell(5, i + 2, col)
                cell = ws.cell(row=5, column=i+2)
                cell.border = border
                cell.font = fontA10
                cell.alignment = alignmentCC
            # for j, row in enumerate(row_headers):
            #     ws.cell(j+6, 2, row)
            #     cell = ws.cell(row=j+6, column=2)
            #     cell.border = border
            if 6 > self.ilDCV.value() > 2:
                row_range = self.ilDCV.value() * 4 + 2
                for row in range(row_range):
                    if row == 0:
                        ws.cell(row + 6, 2, 'mV')
                    elif row == 5:
                        ws.cell(row + 6, 2, 'V')
                    elif row < row_range - 16:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value())
                    elif row < row_range - 12:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value()/100)
                    elif row < row_range - 8:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value()/10)
                    elif row < row_range - 4:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value())
                    elif row < row_range:
                        ws.cell(row + 6, 2, self.zakresDCV.value())
                    cell = ws.cell(row=row+6, column=2)
                    cell.border = border
                    cell.alignment = alignmentCC
                ws.merge_cells("B7:B10")
                ws.merge_cells("B6:F6")
                ws.merge_cells("B11:F11")
                for row in range(row_range + 3):
                    if row > 11 and row % 4 == 0:
                        print(row)
                        ws.merge_cells(f"B{row}:B{row + 3}")

            elif self.ilDCV.value() <= 2:
                row_range = self.ilDCV.value() * 4 + 1
                for row in range(row_range):
                    if row == 0:
                        ws.cell(row + 6, 2, 'V')
                    elif row < row_range - 4:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value())
                    elif row < row_range:
                        ws.cell(row + 6, 2, self.zakresDCV.value())
                    cell = ws.cell(row=row+6, column=2)
                    cell.border = border
                    cell.alignment = alignmentCC
                ws.merge_cells("B6:F6")
                ws.merge_cells("B7:B10")
                ws.merge_cells("B11:B14")

            elif self.ilDCV.value() > 5:
                row_range = self.ilDCV.value() * 4 + 2
                for row in range(row_range):
                    if row == 0:
                        ws.cell(row + 6, 2, 'mV')
                    elif row == 9:
                        ws.cell(row + 6, 2, 'V')
                    elif row < row_range - 25:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value()/100)
                    elif row < row_range - 21:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value()/10)
                    elif row < row_range - 19:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value())
                    elif row < row_range - 12:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value() / 100)
                    elif row < row_range - 8:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value() / 10)
                    elif row < row_range - 4:
                        ws.cell(row + 6, 2, self.zakresDCV_2.value())
                    elif row < row_range:
                        ws.cell(row + 6, 2, self.zakresDCV.value())
                    cell = ws.cell(row=row + 6, column=2)
                    cell.border = border
                    cell.alignment = alignmentCC
                ws.merge_cells("B7:B10")
                ws.merge_cells("B11:B14")
                ws.merge_cells("B6:F6")
                ws.merge_cells("B15:F15")
                for row in range(row_range + 3):
                    if row > 15 and row % 4 == 0:
                        print(row)
                        ws.merge_cells(f"B{row}:B{row + 3}")


        # if self.check_acv.isChecked():
        #     for i, col in enumerate(col_headers):
        #         ws.cell(35, i + 2, col)
        #         cell = ws.cell(row=35, column=i + 2)
        #         cell.border = border
        #         cell.font = fontA10
        #         cell.alignment = alignmentCC
        #     for j, row in enumerate(row_headers):
        #         ws.cell(j + 36, 2, row)
        #         cell = ws.cell(row=j+36, column=2)
        #         cell.border = border




        # ws.column_dimensions['A'].width = 1
        ws.column_dimensions['B'].width = 8
        ws.column_dimensions['C'].width = 13
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 10
        ws.column_dimensions['F'].width = 12

        self.zapis_pliku(self.sciezka_Model.text(), wb)

        wb.close()



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

    def zapis_pliku(self, path, wb):

        # Zapisanie pliku
        if os.path.exists(path + ".xlsx"):
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
                    os.remove(path + ".xlsx")
                    print("Plik już istnieje, nadpisywanie...")
                    wb.save(path + ".xlsx")
                    self.open_folder(path)
                except PermissionError as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Błąd zapisu pliku")
                    msg.setInformativeText(str(e))
                    msg.setWindowTitle("Błąd")
                    msg.exec()
        else:
            print("Plik nie istnieje, zapisywanie...")
            wb.save(path + ".xlsx")
            self.open_folder(path)


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

        ws['B3'] = "ŚWIADECTWO WZORCOWANIA"
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

        # zapis pliku
        self.zapis_pliku(self.sciezkaSW_zapis.text(), wb)

        # # Zapisanie pliku
        # if os.path.exists(self.sciezkaSW_zapis.text() + ".xlsx"):
        #     # Wyświetlenie okna dialogowego z pytaniem o nadpisanie pliku
        #     msg_box = QMessageBox()
        #     msg_box.setText("Plik już istnieje. Czy chcesz go nadpisać?")
        #     msg_box.setWindowTitle("Nadpisać plik?")
        #     msg_box.setIcon(QMessageBox.Question)
        #     msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #     msg_box.setDefaultButton(QMessageBox.No)
        #     # Obsługa wyboru użytkownika
        #     choice = msg_box.exec()
        #     if choice == QMessageBox.Yes:
        #         try:
        #             os.remove(self.sciezkaSW_zapis.text() + ".xlsx")
        #             print("Plik już istnieje, nadpisywanie...")
        #             wb.save(self.sciezkaSW_zapis.text() + ".xlsx")
        #             self.open_folder(self.sciezkaSW_zapis.text())
        #         except PermissionError as e:
        #             msg = QMessageBox()
        #             msg.setIcon(QMessageBox.Critical)
        #             msg.setText("Błąd zapisu pliku")
        #             msg.setInformativeText(str(e))
        #             msg.setWindowTitle("Błąd")
        #             msg.exec()
        # else:
        #     print("Plik nie istnieje, zapisywanie...")
        #     wb.save(self.sciezkaSW_zapis.text() + ".xlsx")
        #     self.open_folder(self.sciezkaSW_zapis.text())




app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()



