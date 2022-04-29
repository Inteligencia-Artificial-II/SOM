import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from src.UI import render_main_window
from src.SOM import SOM
import numpy as np
import pandas as pd

class Plotter:
    def __init__(self):
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)

        # establecemos el color del canvas
        self.ax.set_facecolor("#dedede")

        # definimos la que será una instancia de la clase som
        self.som = None
        # matriz de datos (obtenidos desde un archivo csv)
        self.data = None
        # dimensiones de los datos de entrada
        self.data_shape = None

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
            return

        # lee la información del archivo
        df = pd.read_csv(file)
        # guarda la información en una matriz
        self.data = np.array(df)
        self.data_shape = self.data[0].shape
        self.file_shape['text'] = f'Tamaño: ({self.data.shape[0]}, {self.data.shape[1]})'
        self.init_som()

    def check_topology(self, _):
        """Observa si existen cambios en la topologia de la rejilla"""
        if self.som == None:
            return

        if self.som.grid_topology != self.grid_topology.get():
            self.init_som()

        grid_shape = (int(self.grid_size1.get()), int(self.grid_size2.get()))
        if grid_shape != self.som.grid_shape:
            self.init_som()

    def init_som(self):
        """Inicializa la instancia de SOM y los parámetros del canvas"""
        # obtenemos los datos de la interfaz
        grid_shape = (int(self.grid_size1.get()), int(self.grid_size2.get()))
        topology = self.grid_topology.get()

        # creamos la instancia del SOM
        self.som = SOM(self.data_shape, topology, grid_shape)

        # establecemos los limites de la gráfica
        self.ax.set_xlim([-1, int(self.grid_size1.get())])
        self.ax.set_ylim([-1, int(self.grid_size2.get())])

        # gráficamos la rejilla
        self.draw_grid()

    def draw_grid(self):
        """Dibuja la rejilla en el canvas"""
        # obtenemos el grafo
        neighborhood = self.som.neighborhood
        points = list(neighborhood.graph.keys())

        # limpiamos el canvas
        plt.cla()
        for p in points:
            # obtenemos las coordenadas de la neurona "p"
            x = self.som.neurons[p[0]][p[1]].x
            y = self.som.neurons[p[0]][p[1]].y

            # gráficamos las conexiones del punto "p"
            for dest in neighborhood.GetNeighbors(p):
                # obtenemos las coordenadas de los puntos de destino
                x_dest = self.som.neurons[dest[0]][dest[1]].x
                y_dest = self.som.neurons[dest[0]][dest[1]].y
                plt.plot((x, x_dest), (y, y_dest), color='blue')

        for p in points:
            # obtenemos las coordenadas de la neurona "p"
            x = self.som.neurons[p[0]][p[1]].x
            y = self.som.neurons[p[0]][p[1]].y
            # gráficamos los puntos de origen
            plt.plot(x, y, 'o', color='red')


        # dibujamos los puntos seteados
        self.fig.canvas.draw()

    def run(self):
        """es ejecutada cuando el botón de «entrenar» es presionado"""
        if self.som != None:
            self.som.train(int(self.max_iter.get()), self.data)

    def restart(self):
        """devuelve los valores y elementos gráficos a su estado inicial"""
        pass
