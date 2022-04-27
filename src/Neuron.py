import numpy as np

class Neuron:
    def __init__(self, w_size:tuple, id:int, x:int, y:int):
        # identificador de la neurona
        self.id = id
        # coordenadas de la neurona
        self.x = x
        self.y = y
        # pesos de la neurona
        self.w = np.random.uniform(-1, 1, w_size)

    def __repr__(self):
        return str(self.id)
