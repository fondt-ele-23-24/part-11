from scipy.optimize import brentq

class ShepherEq:
    def __init__(self, r=1, N=1):
        self.r = r
        self.N = N
    
    def __call__(self, x):
        return x - self.r * x / (1 + x**2 / self.N)

    
def find_eq(r, N, a, b):
    f = ShepherEq(r=r, N=N)
    x_sol = brentq(f, a, b)
    return x_sol
    