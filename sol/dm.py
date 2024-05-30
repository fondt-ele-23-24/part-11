import numpy as np
from scipy.optimize import brentq

class DodgeMetzner:
    def __init__(self, Re_pl, n):
        self.Re_pl = Re_pl
        self.n = n
    
    def __call__(self, f):
        A = 1 / np.sqrt(f)
        B = - 4 / self.n**0.75 * np.log(self.Re_pl * f**(1 - self.n / 2))
        C = 0.4 / self.n**1.2
        return A + B + C

    
def find_sol(Re_pl, n):
    f = DodgeMetzner(Re_pl=Re_pl, n=n)
    x_sol = brentq(f, a=0.001, b=0.003)
    return x_sol
    