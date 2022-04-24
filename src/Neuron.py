import numpy as np

class Neuron:
    def __init__(self, w_size:tuple):
        # pesos de la neurona
        self.w = np.random.uniform(-1, 1, w_size)
        