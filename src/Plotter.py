import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from src.UI import render_main_window
from src.SOM import SOM
import numpy as np
import pandas as pd

class Plotter:
    def __init__(self):
        # punto mínimo y máximo del canvas
        self.ax_max = 5
        self.ax_min = -5
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        # establecemos los limites de la gráfica
        self.ax.set_xlim([self.ax_min, self.ax_max])
        self.ax.set_ylim([self.ax_min, self.ax_max])
        # establecemos el color del canvas
        self.ax.set_facecolor("#dedede")

        # definimos la que será una instancia de la clase som
        self.som = None
        # matriz de datos (obtenidos desde un archivo csv)
        self.data = None

        # valores por defecto para la interfaz
        self.default_grid_topology = "Cruz"
        self.default_max_iter = 100
        self.default_grid_size = 5

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
            shape = self.data.shape
            self.file_shape['text'] = f'Tamaño: ({shape[0]}, {shape[1]})'
            # creamos la instancia del SOM
            grid_shape = (int(self.grid_size1.get()), int(self.grid_size2.get()))
            self.som = SOM(shape, self.grid_topology.get(), grid_shape)

    def run(self):
        """es ejecutada cuando el botón de «entrenar» es presionado"""
        pass

    def restart(self):
        """devuelve los valores y elementos gráficos a su estado inicial"""
        pass
