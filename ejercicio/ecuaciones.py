import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class Ecuaciones_diferenciales:
    def ecuacion4():
        t = sp.Symbol('t') ; y = sp.Function('y')
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        print(f" La solución es {sp.dsolve(ecuacion, y(t))}")
        t = np.linspace(0, 2, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel('t') ; plt.ylabel('y')
        plt.title('Ecuación diferencial 2ty\'- y = 3t**2')
        plt.grid() ; plt.show()




Ecuaciones_diferenciales.ecuacion1()
