from matplotlib import pyplot as plt
import numpy as np

def plot_univariate_function(f, x, figsize=None):
    plt.figure(figsize=figsize)
    plt.plot(x, f(x))
    plt.plot(plt.xlim(), [0, 0])
    plt.grid()
    plt.show()

    
    
def bisection(f, a, b, tol=1e-6):
    # Controllo le condizioni di applicabilità
    if f(a) * f(b) >= 0:
        print('f(a) e f(b) devono avere segno opposto')
        return None
    # Individuo uno zero
    while abs(a - b) > tol:
        m = 0.5 * (a + b)
        if f(m) * f(a) >= 0:
            a = m
        else:
            b = m
    # Restituisco la soluzione
    return m

    
def bisection_with_plot(f, a, b, tol=1e-6, max_it=100, figsize=None):
    # Controllo le condizioni di applicabilità
    if f(a) * f(b) >= 0:
        print('f(a) e f(b) devono avere segno opposto')
        return None
    # Individuo uno zero
    midpoints = [a, b]
    a0, b0 = a, b
    for k in range(max_it):
        m = 0.5 * (a + b)
        midpoints.append(m)
        if f(m) * f(a) >= 0:
            a = m
        else:
            b = m
        if abs(a -b) <= tol:
            break
    # Disegno i passi del procedimento
    x = np.linspace(a0, b0, 1000)
    plt.figure(figsize=figsize)
    plt.plot(x, f(x))
    plt.plot(plt.xlim(), [0, 0])    
    plt.vlines(midpoints, ymin=plt.ylim()[0], ymax=plt.ylim()[1],
               color='tab:red', linestyle=':')
    plt.grid()
    plt.show()
    # Restituisco la soluzione
    return m


def num_der(f, x):
    h = np.sqrt(np.finfo(float).eps)
    df = f(x+h) - f(x)
    return df / h


def nrm_univariate(f, x0, tol=1e-6, max_it=100):
    # Parto dalla stima iniziale
    x = x0
    # Facciamo al più max_it iterazioni
    for k in range(max_it):
        # Passo principale del metodo di Newton-Raphson
        nx = x - f(x) / num_der(f, x)
        # Controllo la condizione di terminazione 
        if abs(nx - x) <= tol:
            break
        # Rimpiazzo x con il nuovo valore
        x = nx
    return x


def nrm_univariate_with_plot(f, x0, a, b, tol=1e-6, max_it=100, figsize=None):
    # Parto dalla stima iniziale
    x = x0
    hx = []
    hd = []
    # Facciamo al più max_it iterazioni
    for k in range(max_it):
        # Memorizzo il punto corrente
        hx.append(x)
        # Calcolo la derivata
        fp = num_der(f, x)
        # Memorizzo il valore della derivata
        hd.append(fp)
        # Passo principale del metodo di Newton-Raphson
        nx = x - f(x) / fp
        # Controllo la condizione di terminazione 
        if abs(nx - x) <= tol:
            break
        # Rimpiazzo x con il nuovo valore
        x = nx
    # Disegno i passi del procedimento
    xr = np.linspace(a, b, 1000)
    plt.figure(figsize=figsize)
    plt.plot(xr, f(xr))
    plt.plot(plt.xlim(), [0, 0])
    # Disegno i punti visitati
    xv = np.array(hx + [x])
    plt.scatter(xv, f(xv), color='tab:red')
    # Disegno le tangengi
    for xk, dk in zip(hx, hd):
        y = f(xk) + dk * (xr - xk)
        plt.plot(xr, y, color='tab:red', linestyle=':')
    plt.grid()
    plt.show()
    return x
    








    