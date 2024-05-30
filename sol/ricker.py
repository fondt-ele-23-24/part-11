import numpy as np
from scipy.optimize import brentq

class RickerEq:
    def __init__(self, r=1, N=1):
        self.r = r
        self.N = N
    
    def __call__(self, x):
        return x - x * np.exp(1 - x / self.N)

    
def find_eq(r, N, a, b):
    f = RickerEq(r=r, N=N)
    x_sol = brentq(f, a, b)
    return x_sol
    