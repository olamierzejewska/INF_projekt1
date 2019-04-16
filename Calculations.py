# Ten plik przeprowadza obliczenia matematyczne potrzebne do zrealizowania zadania.
import numpy as np

# Klasa przeprowadzająca obliczenia matematyczne w celu znalezienia przecięcia danych odcinków lub stwierdzenia, że
# są równoległe.
class Calculations:
    # Konstruktor przyjmuje dane do przetworzenia w formacie [XA, YA, XB, YB, XC, YC, XD, YD]
    def __init__(self, data):
        self.wczytajPunkty(data)

    # Przypisuje wartości przekazane do funkcji zmiennym wewnętrznym self.XA...self.YD
    def wczytajPunkty(self, data):
        self.XA = data[0]  # 1186,00
        self.YA = data[1]  # 17962,69
        self.XB = data[2]  # 1144,74
        self.YB = data[3]  # 18006,22
        self.XC = data[4]  # 1184,31
        self.YC = data[5]  # 18004,14
        self.XD = data[6]  # 1151,14
        self.YD = data[7]  # 17957,41

    # Przeprowadza obliczenia na klasie. Zwraca wartości (XP, YP, nr komunikatu)
    def przetworz(self):
        print("przetwórz wew klasy")
        dXAB = self.XB - self.XA
        dYAB = self.YB - self.YA
        dXAC = self.XC - self.XA
        dYAC = self.YC - self.YA
        dXCD = self.XD - self.XC
        dYCD = self.YD - self.YC

        if (dXAB * dYCD - dYAB * dXCD) == 0:
            komunikat = 0
            print(" ", komunikat)
            return 0,0,0

        if (dXAB * dYCD - dYAB * dXCD) != 0:
            t1 = (dXAC * dYCD - dYAC * dXCD) / (dXAB * dYCD - dYAB * dXCD)
            t2 = (dXAC * dYAB - dYAC * dXAB) / (dXAB * dYCD - dYAB * dXCD)
            print("t1 = ", t1)
            print("t2 = ", t2)

        if (t1 >= 0 and t1 <= 1) and (t2 >= 0 and t2 <= 1):
            komunikat = 1

        elif ((t1 >= 0 and t1 <= 1) and (t2 < 0 or t2 > 1)) or ((t1 < 0 or t1 > 1) and (t2 >= 0 and t2 <= 1)):
            komunikat = 2

        else:
            komunikat = 3

        self.XP = self.XA + t1 * dXAB
        self.YP = self.YA + t1 * dYAB

        print("XP = ", self.XP)  # 1168,210
        print("YP = ", self.YP)  # 17981,459

        return self.XP, self.YP, komunikat