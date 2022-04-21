import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from src.UI import render_main_window
from src.SOM import SOM
import numpy as np
import pandas as pd

class Plotter:
    def __init__(self):
        self.ax_max = 5
        self.ax_min = -5
        self.fig = plt.figure(1)
        self.fig2 = plt.figure(2)
        self.ax = self.fig.add_subplot(111)
        self.ax2 = self.fig2.add_subplot(111)
        # establecemos los limites de la gráfica
        self.ax.set_xlim([self.ax_min, self.ax_max])
        self.ax.set_ylim([self.ax_min, self.ax_max])
        self.ax.set_facecolor("#dedede")
        self.ax2.set_facecolor("#dedede")

        # definimos la que será una instancia de la clase som
        self.som = None
        # matriz de datos (obtenidos desde un archivo csv)
        self.data = None

        # inicializamos la ventana principal
        self.window = Tk()
        render_main_window(self)
        self.window.mainloop()

    def open_file(self):
        """Abre el explorador de archivos y guarda
        la información de los archivos selecionados"""
        # obtiene la dirección donde se encuentra un archivo
        file = filedialog.askopenfilename(
            initialdir='./', title='select a file',
            filetypes=(('csv files', '*.csv'), ('all files', '*.*')))

        if file[-3:] != 'csv':
            print("Error: el archivo debe ser .csv")
        else:
            # lee la información del archivo
            df = pd.read_csv(file)
            # guarda la información en una matriz
            self.data = np.array(df)
            print("data: ", self.data)

    def run(self):
        """es ejecutada cuando el botón de «entrenar» es presionado"""
        pass

    def restart(self):
        """devuelve los valores y elementos gráficos a su estado inicial"""
        pass
