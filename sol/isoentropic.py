import numpy as np
from scipy.optimize import fsolve

class Isoentropic:
    def __init__(self, p, T, p0, T0, z0z, R, g):
        self.p = p
        self.T = T
        self.p0 = p0
        self.T0 = T0
        self.z0z = z0z
        self.R = R
        self.g = g
    
    def __call__(self, X):
        # Spacchetto le due variabili
        gm, M = X
        # Valore dell'espressione interna
        v = 1 + (1 - 1/gm) * M / (self.R * self.T0) * self.g * self.z0z
        # Valore della prima equazione
        vp = self.p - self.p0 * v**(gm / (gm - 1))
        # Valore della seconda equazione
        vT = self.T - self.T0 * v
        return np.array([vp, vT])

    
def find_sol(p, T, p0, T0, z0z, R, g):
    f = Isoentropic(p, T, p0, T0, z0z, R, g)
    x0 = [1.3, 18]
    x_sol = fsolve(f, x0)
    if np.abs(f(x_sol)).max() <= 1e-6:
        return x_sol
    else:
        return None
        
    