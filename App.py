# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:48:54 2019

@author: ToshibaPC
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QColorDialog, QFileDialog, QErrorMessage, QSizePolicy
import matplotlib.pyplot as plt
import Calculations
import Plot


# Klasa aplikacji dziedzicząca z QWidget odpowiada za organizację interfejsu graficznego i komunikację z komponentami
class AppWindow(QWidget):

    # Inicjalizacja GUI
    def __init__(self):
        super().__init__()
        self.canvas = Plot.Canvas(self, width=8, height=8)
        self.title = 'WYZNACZENIE PUNKTU PRZECIĘCIA DWÓCH ODCINKÓW'
        self.initInterface()
        self.initWidgets()
        
    # Określenie podstawowych parametrów okna
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 900, 500)
        self.show()

    # Utworzenie i rozmieszczenie w siatce elementów interfejsu
    def initWidgets(self):

        # Labels
        self.Odc1Label = QLabel("Odcinek AB:")
        self.Odc2Label = QLabel("Odcinek CD:")
        self.PPLabel = QLabel("Punkt przecięcia odcinków:")
        self.TypPPLabel = QLabel("")
        self.AXLabel = QLabel("XA")
        self.AYLabel = QLabel("YA")
        self.BXLabel = QLabel("XB")
        self.BYLabel = QLabel("YB")
        self.CXLabel = QLabel("XC")
        self.CYLabel = QLabel("YC")
        self.DXLabel = QLabel("XD")
        self.DYLabel = QLabel("YD")
        self.PXLabel = QLabel("XP")
        self.PYLabel = QLabel("YP")
        self.FileLabel = QLabel("Uzupełnij dane z pliku")
        self.FileNameLabel = QLabel("")

        # Buttons + button connects
        FileBtn = QPushButton("Otwórz plik", self)
        DrawBtn = QPushButton("Oblicz i rysuj", self)
        CleanBtn = QPushButton("Wyczyść", self)
        SaveBtn = QPushButton("Zapisz", self)
        btnCol1 = QPushButton("Zmień kolor odcinka AB", self)          
        btnCol2 = QPushButton("Zmień kolor odcinka CD", self) 

        FileBtn.clicked.connect(self.uzupelnijZPliku)
        DrawBtn.clicked.connect(self.sprawdzPoprawnosc)
        CleanBtn.clicked.connect(self.wyczysc)
        SaveBtn.clicked.connect(self.zapisz)
        btnCol1.clicked.connect(self.colorAB)
        btnCol2.clicked.connect(self.colorCD)
  
        # Edits
        self.XAEdit = QLineEdit()
        self.YAEdit = QLineEdit()
        self.XBEdit = QLineEdit()
        self.YBEdit = QLineEdit()
        self.XCEdit = QLineEdit()
        self.YCEdit = QLineEdit()
        self.XDEdit = QLineEdit()
        self.YDEdit = QLineEdit()
        self.XPEdit = QLineEdit()
        self.YPEdit = QLineEdit()

        # Grids
        grid = QGridLayout() # ustawienie typu rozmieszczenia elementów

        # Określenie minimalnych szerokości kolumn
        grid.setColumnMinimumWidth(0, 6)
        grid.setColumnMinimumWidth(1, 20)
        grid.setColumnMinimumWidth(2, 6)
        grid.setColumnMinimumWidth(3, 20)
        grid.setColumnMinimumWidth(4, 20)

        # Rozmieszczenie elementów w wierszach i kolumnach
        i = 0 
        grid.addWidget(self.Odc1Label, i, 0, 1, 4)

        i += 1
        grid.addWidget(self.AXLabel, i, 0)
        grid.addWidget(self.XAEdit, i, 1)
        grid.addWidget(self.AYLabel, i, 2)
        grid.addWidget(self.YAEdit, i, 3)

        i += 1
        grid.addWidget(self.BXLabel, i, 0)
        grid.addWidget(self.XBEdit, i, 1)
        grid.addWidget(self.BYLabel, i, 2)
        grid.addWidget(self.YBEdit, i, 3)

        i += 1
        grid.addWidget(self.Odc2Label, i, 0, 1, 4)
        i += 1
        grid.addWidget(self.CXLabel, i, 0)
        grid.addWidget(self.XCEdit, i, 1)
        grid.addWidget(self.CYLabel, i, 2)
        grid.addWidget(self.YCEdit, i, 3)

        i += 1
        grid.addWidget(self.DXLabel, i, 0)
        grid.addWidget(self.XDEdit, i, 1)
        grid.addWidget(self.DYLabel, i, 2)
        grid.addWidget(self.YDEdit, i, 3)

        i += 1
        grid.addWidget(DrawBtn, i, 0, 1, 4)

        i += 1
        grid.addWidget(self.PPLabel, i, 0, 1, 4)

        i += 1
        grid.addWidget(self.PXLabel, i, 0)
        grid.addWidget(self.XPEdit, i, 1)
        grid.addWidget(self.PYLabel, i, 2)
        grid.addWidget(self.YPEdit, i, 3)

        i += 1
        grid.addWidget(self.TypPPLabel, i, 0, 1, 6)
        
        grid.addWidget(self.FileLabel, 0, 5)
        grid.addWidget(FileBtn, 1, 5)
        grid.addWidget(self.FileNameLabel, 1, 7)
        grid.addWidget(btnCol1, 10, 0, 2, 4)
        grid.addWidget(btnCol2, 12, 0, 2, 4)
        grid.addWidget(CleanBtn, 5, 5)
        grid.addWidget(SaveBtn, 8, 5)
        
        grid.addWidget(self.canvas, 2, 7, 20, 1)

        # Ustawienia dotyczące rozmieszczenia siatkowego
        self.setLayout(grid)
        
    # Funkcja przyjmująca dane do wyrysowania z klasy wywołującej przez argument data[], przypisuje otrzymane wartości
    # współrzędnych XA...YP zmiennym wewnętrznym. Wywołuje funkcję rysującą.
    def aktualizuj(self, data):
        print("aktualizuj")
        print(data)
        self.XA = data[0]
        self.YA = data[1]
        self.XB = data[2]
        self.YB = data[3]
        self.XC = data[4]
        self.YC = data[5]
        self.XD = data[6]
        self.YD = data[7]
        self.XP = data[8]
        self.YP = data[9]
        self.plot()
        
    # Funkcja zmienia kolor odcinka. Jest wywoływana przez naciśnięcie ColorBtn  
    def colorAB(self):
            colorAB= QColorDialog.getColor()
            if colorAB.isValid():
                print(colorAB.name())
                #self.col1 = colorAB.name()
                self.draw(col1=colorAB.name())

    def colorCD(self):
            colorCD= QColorDialog.getColor()
            if colorCD.isValid():
                print(colorCD.name())
                #self.col2 = colorCD.name()
                self.plot(col2=colorCD.name())
    
    # Funkcja usuwa zawartość pól do wprowadzania współrzędnych punktów A, B, C, D oraz wyniku P. Jest wywoływana przez
    # inne funkcje w razie potrzeby wyczyszczenia danych, w szczególności przez funkcję wyczyść.
    def wyczyscEdits(self):
        self.XAEdit.clear()
        self.YAEdit.clear()
        self.XBEdit.clear()
        self.YBEdit.clear()
        self.XCEdit.clear()
        self.YCEdit.clear()
        self.XDEdit.clear()
        self.YDEdit.clear()
        self.XPEdit.clear()
        self.YPEdit.clear()

    # Funkcja usuwa zawartość pól do wprowadzania współrzędnych punktu P oraz komunikatu o typie przecięcia odcinków.
    # Jest wywoływana przez inne funkcje w razie potrzeby.
    def wyczyscWynik(self):
        self.XPEdit.setText("")
        self.YPEdit.setText("")
        self.wyczyscInformacje()

    # Funkcja usuwa zawartość komunikatu o typie przecięcia odcinków.
    def wyczyscInformacje(self):
        self.TypPPLabel.setText("")

    # Funkcja usuwa wypisaną nazwę pliku wykorzystanego do wprowadzenia danych.
    def wyczyscFilename(self):
        self.FileNameLabel.setText("")

    # Funkcja usuwa wszystkie dane wprowadzone przez użytkownika oraz zwrócone w wyniku wykonania programu.
    def wyczysc(self):
        self.wyczyscEdits()
        self.wyczyscWynik()
        self.wyczyscFilename()

    # Funkcja wywołuje okienko, z którego można wczytać plik z danymi do przeliczenia oraz wypisuje wartości z tego
    # pliku. Jest wywoływana przez FileBtn. Wypisuje nazwę i ścieżkę do otwartego pliku pod buttonem.
    def uzupelnijZPliku(self):
        self.wyczyscEdits()
        fileName = QFileDialog.getOpenFileName(None, "Wybierz plik z danymi", "/aaa/", "Text Files (*.txt)")
        self.FileNameLabel.setText(fileName[0])

        file = open(fileName[0], 'r')
        self.XAEdit.insert(file.readline())
        self.YAEdit.insert(file.readline())
        self.XBEdit.insert(file.readline())
        self.YBEdit.insert(file.readline())
        self.XCEdit.insert(file.readline())
        self.YCEdit.insert(file.readline())
        self.XDEdit.insert(file.readline())
        self.YDEdit.insert(file.readline())
        file.close()

    # Funkcja sprawdza, czy string jest konwertowalny do float.
    def czyFloat(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    # Funkcja przyjmuje wartośći wprowadzone przez użytkownika typu string i sprawdza, czy jest możliwa ich konwersja do
    # float. Jeśli tak, przekształca je w tablicę wartości typu float i wywołuje funkcję do przeprowadzenia obliczeń
    # przekazując jej wartości. Jeśli nie, zwraca fałsz i powraca do widoku.
    def sprawdzPoprawnosc(self, val):
        self.TypPPLabel.setText("")
        data = []
        data.append(self.XAEdit.text())
        data.append(self.YAEdit.text())
        data.append(self.XBEdit.text())
        data.append(self.YBEdit.text())
        data.append(self.XCEdit.text())
        data.append(self.YCEdit.text())
        data.append(self.XDEdit.text())
        data.append(self.YDEdit.text())

        for i in data:
            if not self.czyFloat(i):
                self.wyczyscWynik()
                self.TypPPLabel.setText("Błędny format danych!")
                return False

        floatData = [] # nowa tablica wartości zamienionych na float
        for i in range(8):
            floatData.append(float(data[i]))

        # przekazanie danych do obliczeń
        self.przetworz(floatData)

    # Funkcja dopisuje do pliku w trybie append o ile wartości wyniku są poprawne. W przeciwnym wypadku zwraca fałsz
    # i wypisuje komunikat.
    def zapisz(self):
        x = self.XPEdit.text()
        y = self.YPEdit.text()
        print(x, y)
        if self.czyFloat(x) and self.czyFloat(y):
            name = QFileDialog.getSaveFileName(self, 'Zapisz do pliku', "/", "Text Files (*.txt)")
            file = open(name[0], 'a')
            file.write(38 * '-')
            file.write("\n| {} | {:^8s} | {:^8s} |\n".format("Nazwa punktu", "X [m]", "Y [m]"))
            file.write(38 * '-')
            file.write("\n| {:^12} | {:^8.3f} | {:^8.3f} |\n".format("P", float(x), float(y)))
            file.write(38 * '-')
            file.write("\n")
            file.close()
            return True
        else:
            self.TypPPLabel.setText("Błędny format wyniku - błąd zapisu")
            return False

    # Funkcja wywołuje konstruktor klasy Calculations i przekazuje jej dane do przeliczenia. Zwrócony wynik analizuje
    # pod kątem typu przecięcia i wypisuje informację oraz ewentualny punkt przecięcia. Następnie wywołuje metodę
    # rysującą wykres.
    def przetworz(self, data):
        model = Calculations.Calculations(data)

        result = model.przetworz() # dane zwrócone (XP, YP, nr komunikatu)
        data.append(float(result[0])) # dodanie punktu przecięcia do listy danych do narysowania
        data.append(float(result[1]))

        self.TypPPLabel.clear()
        if result[2] == 0:
            self.TypPPLabel.setText("Odcinki są równoległe")

        else:
            self.XPEdit.setText(str(round(result[0], 3)))
            self.YPEdit.setText(str(round(result[1], 3)))

            if result[2] == 1:
                self.TypPPLabel.setText("Punkt należy do obu odcinków")

            elif result[2] == 2:
                self.TypPPLabel.setText("Punkt należy do jednego odcinka i leży na przedłużeniu drugiego odcinka")

            elif result[2] == 3:
                self.TypPPLabel.setText("Punkt leży na przecięciu przedłużeń obu odcinków")

            self.canvas.aktualizuj(data) # komunikuje się z klasą wykresu o ile odcinki nie są równoległe

# Inicjalizacja programu
if __name__=='__main__':
    app = QApplication(sys.argv)
    okno = AppWindow()
    sys.exit(app.exec_())