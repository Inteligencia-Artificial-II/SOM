import numpy as np
from src.Graph import Graph
from src.Neuron import Neuron

class SOM:
    def __init__(self, w_size:tuple, topology:str, shape:tuple):
        # parámetros de la rejilla
        self.grid_shape = shape
        self.grid_topology = topology
        # tamaño del vector de pesos de las neuronas
        self.weights_size = w_size

        # vecindario de neuronas
        self.neighborhood = Graph()
        self.id = 0

        self.neurons = []

        # neurona ganadora por iteración
        self.bmu = None

        self.create_neighborhood()

    def create_star_topology(self):
        """Añade las conexiones en diagonal al grafo"""
        for i in range(1, self.grid_shape[0]):
            for j in range(self.grid_shape[1]):
                # Se revisa que los índices no sean negativos
                if j - 1 >= 0:
                    self.neighborhood.CreateEdge((i, j), (i - 1, j - 1), 1)
                if j + 1 < self.grid_shape[1]:
                    self.neighborhood.CreateEdge((i, j), (i - 1, j + 1), 1)

    def create_cross_topology(self):
        """Añade las conexiones verticales y horizontales al grafo"""
        # crea la topologia de cruz para la rejilla
        for i in range(self.grid_shape[0]):
            row = []
            for j in range(self.grid_shape[1]):
                row.append(Neuron(self.weights_size, self.get_id()))

                # fila actual
                if j < self.grid_shape[1] - 1:
                    self.neighborhood.CreateEdge((i, j),(i, j + 1), 1)
                # filas previas
                if i > 0:
                    prev_row = i - 1
                    self.neighborhood.CreateEdge((i, j),(prev_row, j), 1)
            self.neurons.append(row[:])

    def create_neighborhood(self):
        """Usa los parámetros de la rejilla
           para crear un gráfo"""
        self.create_cross_topology()
        if self.grid_topology == "Estrella":
            self.create_star_topology()

    def get_id(self):
        """Obtiene un identificador único para 
           las instancias de las neuronas"""
        self.id += 1
        return self.id

    def train(self):
        """Función que entrena la red"""
        pass
