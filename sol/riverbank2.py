import numpy as np
from scipy.optimize import fsolve

class Riverbank:
    def __init__(self, x0, y0, y1, ymax, s):
        self.x0 = x0
        self.y0 = y0
        self.y1 = y1
        self.ymax = ymax
        self.s = s
    
    def __call__(self, X):
        # Spacchetto le due variabili
        a2, a1, a0, x1, xm = X
        # Calcolo le funzioni associate ad ogni condizione
        c1 = a2 * self.x0**2 + a1 * self.x0 + a0 - self.y0
        c2 = a2 * x1**2 + a1 * x1 + a0 - self.y1
        c3 = 2 * a2 * xm + a1
        c4 = a2 * xm**2 + a1 * xm + a0 - self.ymax
        c5 = a2/3 * x1**3 + a1/2 * x1**2 + a0 * x1 - self.s
        return np.array([c1, c2, c3, c4, c5])

    
def find_sol(x0, y0, y1, ymax, s):
    f = Riverbank(x0, y0, y1, ymax, s)
    x0 = [-1, 1, 0, 3, 6]
    x_sol = fsolve(f, x0)
    if np.abs(f(x_sol)).max() <= 1e-6:
        return x_sol
    else:
        return None
        
    