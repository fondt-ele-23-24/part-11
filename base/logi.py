import numpy as np

class LogiEq:
    def __init__(self, r=1, N=1):
        self.r = r
        self.N = N
    
    def __call__(self, x):
        return x - self.r * x * (1 - x/self.N)
