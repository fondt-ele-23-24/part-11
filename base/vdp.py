import numpy as np

class VdPEq:
    def __init__(self, mu=1):
        self.mu = mu
    
    def __call__(self, X):
        x, y = X
        dx = y
        dy = self.mu * (1 - x**2) * y - x
        return np.array([dx, dy])
