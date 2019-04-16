# Ten plik rysuje wykres z pomocą biblioteki matplotlib w module wbudowanym w GUI. Dziedziczy z modułu PyQT5
# FigureCanvas.
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Klasa przyjmuje przez funkcję aktualizuj dane do wyrysowania na wykresie wbudowanym w GUI i rysuje wykres.
class Canvas(FigureCanvas):
    # Inicjalizacja wykresu
    def __init__(self, parent=None, width=8, height=8, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.aktualizuj([0,0,0,0,0,0,0,0,0,0]) # wykres widoczny po otwarciu programu

    # Funkcja rysująca wykres
    def plot(self):
        self.fig.clear()
        self.col1='r'
        self.col2='b'

        ax = self.figure.add_subplot(111)
        ax.set_title('Wizualizacja')
        ax.set_xlabel('współrzędna y')
        ax.set_ylabel('współrzędna x')

        ax.plot([self.YA, self.YP], [self.XA, self.XP], 'yo:')
        ax.plot([self.YB, self.YP], [self.XB, self.XP], 'yo:')
        ax.plot([self.YC, self.YP], [self.XC, self.XP], 'yo:')
        ax.plot([self.YD, self.YP], [self.XD, self.XP], 'yo:')
        ax.plot([self.YA, self.YB], [self.XA, self.XB], color=self.col1, marker='o')
        ax.plot([self.YC, self.YD], [self.XC, self.XD], color=self.col2, marker='o')

        # etykiety
        ax.annotate('A({:.1f}, {:.1f})'.format(self.XA, self.YA), [self.YA, self.XA])
        ax.annotate('B({:.1f}, {:.1f})'.format(self.XB, self.YB), [self.YB, self.XB])
        ax.annotate('C({:.1f}, {:.1f})'.format(self.XC, self.YC), [self.YC, self.XC])
        ax.annotate('D({:.1f}, {:.1f})'.format(self.XD, self.YD), [self.YD, self.XD])
        ax.annotate('P({:.1f}, {:.1f})'.format(self.XP, self.YP), [self.YP, self.XP])

        self.draw()
        
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
