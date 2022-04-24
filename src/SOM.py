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

        # neurona ganadora por iteración
        self.bmu = None
    
    def create_neighborhood(self):
        """Usa los parámetros de la rejilla
           para crear un gráfo"""
        pass

    def train(self):
        """Función que entrena la red"""
        pass
