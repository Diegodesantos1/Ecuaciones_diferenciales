import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math
class Ecuaciones:
    def ecuacion1():
        x = sp.Symbol("x") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(x).diff(x), (y * (x**2) - y)/(y + 1))
        ics = {y(3): -1}
        print(f" La solución de la primera ecuación es {sp.dsolve(ecuacion, y(t), ics=ics)}")
        t = np.linspace(0, 4, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel("t") ; plt.ylabel("y")
        plt.title("1a Ecuación Diferencial", fontsize=20, color="blue")
        plt.grid() ; plt.show()
    def ecuacion2():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) * sp.sin(t), y(t) * sp.log(y(t)))
        ics = {y((math.pi/2)): math.e}
        print(f" La solución de la segunda ecuación es {sp.dsolve(ecuacion, y(t), ics=ics)}")
        t = np.linspace(0, 2, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel("t") ; plt.ylabel("y")
        plt.title("2a Ecuación Diferencial", fontsize=20, color="green")
        plt.grid() ; plt.show()
    def ecuacion3():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2)
        print(f" La solución de la tercera ecuación es {sp.dsolve(ecuacion, y(t))}")
        t = np.linspace(0, 4, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel("t") ; plt.ylabel("y")
        plt.title("3a Ecuación Diferencial", fontsize=10, color="red")
        plt.grid() ; plt.show()
    def ecuacion4():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        print(f" La solución de la cuarta ecuación es {sp.dsolve(ecuacion, y(t))}")
        t = np.linspace(0, 2, 100) ; y = 1/3*t**3 + 1/3*t**2
        plt.plot(t, y) ; plt.xlabel("t") ; plt.ylabel("y")
        plt.title("4a Ecuación Diferencial", fontsize=10, color="purple")
        plt.grid() ; plt.show()

Ecuaciones.ecuacion1()
Ecuaciones.ecuacion2()
Ecuaciones.ecuacion3()
Ecuaciones.ecuacion4()
