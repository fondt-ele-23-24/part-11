import numpy as np
from scipy.optimize import fsolve

class Riverbank:
    def __init__(self, x0, x1, y0, y1, ymax):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.ymax = ymax
    
    def __call__(self, X):
        # Spacchetto le due variabili
        a2, a1, a0, x2 = X
        # Calcolo le funzioni associate ad ogni condizione
        c1 = a2 * self.x0**2 + a1 * self.x0 + a0 - self.y0
        c2 = a2 * self.x1**2 + a1 * self.x1 + a0 - self.y1
        c3 = 2 * a2 * x2 + a1
        c4 = a2 * x2**2 + a1 * x2 + a0 - self.ymax
        return np.array([c1, c2, c3, c4])

    
def find_sol(x0, x1, y0, y1, ymax):
    f = Riverbank(x0, x1, y0, y1, ymax)
    x0 = [-1, 1, 0, 3]
    x_sol = fsolve(f, x0)
    if np.abs(f(x_sol)).max() <= 1e-6:
        return x_sol
    else:
        return None
        
    