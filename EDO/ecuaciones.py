import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import *
import math
class Ecuaciones:
    def ecuacion1():
        x = sp.Symbol("x") ; y = sp.Symbol("y")
        e1 = integrate((1 + 1/y), y) ; e2 = integrate((x**2 - 1), x)
        ecuacion = sp.Eq(e1, e2) ; sol = sp.solve(ecuacion, y)
        print(f" La solución de la primera ecuación es: \n\n\n")
        sp.pprint(sol)
    def ecuacion2():
        x = sp.Symbol("x") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(x).diff(x) * sp.sin(x), y(x) * sp.log(y(x)))
        ics = {y((math.pi/2)): math.e} ; sol = sp.dsolve(ecuacion, y(x), ics=ics)
        print(f" La solución de la segunda ecuación es: \n\n\n")
        sp.pprint(sol)
    def ecuacion3():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2) ; sol = sp.dsolve(ecuacion, y(t))
        print(f" La solución de la tercera ecuación es: \n\n\n")
        sp.pprint(sol)
    def ecuacion4():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2) ; sol = sp.dsolve(ecuacion, y(t))
        print(f" La solución de la cuarta ecuación es: \n\n\n")
        sp.pprint(sol)
        t = np.linspace(0, 1, 100) ; y1 = 3*t**2/2 ; y2 = 3*t**2/2 + 3*t**3/2
        y3 = 3*t**2/2 + 3*t**3/2 + 3*t**4/2 ; y4 = 3*t**2/2 + 3*t**3/2 + 3*t**4/2 + 3*t**5/2
        plt.plot(t, y1, label="y1(t)") ; plt.plot(t, y2, label="y2(t)")
        plt.plot(t, y3, label="y3(t)") ; plt.plot(t, y4, label="y4(t)")
        plt.title("Familia de soluciones de la ecuación diferencial", fontsize=15, color="blue") ; plt.legend() ; plt.grid() ; plt.show()

