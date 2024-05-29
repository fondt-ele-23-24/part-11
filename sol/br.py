import numpy as np
from scipy.optimize import brentq

class BuckinghamReiner:
    def __init__(self, Re, He):
        self.Re = Re
        self.He = He
    
    def __call__(self, f):
        return f - 64/self.Re * (1 + 1/6 * self.He / self.Re - 64/3 * self.He**4 / (f**3 * self.Re**7))

    
def find_sol(Re, He):
    f = BuckinghamReiner(Re=Re, He=He)
    x_sol = brentq(f, a=0.001, b=0.004)
    return x_sol
    