import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class Ecuaciones_diferenciales:
    def ecuacion1():
        pass
    def ecuacion2():
        pass
    def ecuacion3():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2)
        print(f" La solución de la tercera ecuación es {sp.dsolve(ecuacion, y(t))}")
        t = np.linspace(0, 4, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel('t') ; plt.ylabel('y')
        plt.title('Ecuación diferencial y\' - (y/(t-2)) = 2(t-2)**2', fontsize=10, color='blue')
        plt.grid() ; plt.show()
    def ecuacion4():
        t = sp.Symbol('t') ; y = sp.Function('y')
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        print(f" La solución de la cuarta ecuación es {sp.dsolve(ecuacion, y(t))}")
        t = np.linspace(0, 2, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel('t') ; plt.ylabel('y')
        plt.title('Ecuación diferencial 2ty\'- y = 3t**2 : FAMILIA DE SOLUCIONES', fontsize=10, color='blue')
        plt.grid() ; plt.show()

Ecuaciones_diferenciales.ecuacion3()
Ecuaciones_diferenciales.ecuacion4()
