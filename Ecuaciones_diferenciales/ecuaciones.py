from numbers import Integral
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import *
import math
class Ecuaciones:
    def ecuacion1():
        x = sp.Symbol("x") ; y = sp.Symbol("y")
        e1 = integrate((1 + 1/y), y) ; e2 = integrate((x**2 - 1), x)
        ecuacion = sp.Eq(e1, e2)
        print(f" La solución de la primera ecuación es {sp.solve(ecuacion, y)}")
    def ecuacion2():
        x = sp.Symbol("x") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(x).diff(x) * sp.sin(x), y(x) * sp.log(y(x)))
        ics = {y((math.pi/2)): math.e}
        print(f" La solución de la segunda ecuación es {sp.dsolve(ecuacion, y(x), ics=ics)}")
    def ecuacion3():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2)
        print(f" La solución de la tercera ecuación es {sp.dsolve(ecuacion, y(t))}")
    def ecuacion4():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        print(f" La solución de la cuarta ecuación es {sp.dsolve(ecuacion, y(t))}")

Ecuaciones.ecuacion1()
Ecuaciones.ecuacion2()
Ecuaciones.ecuacion3()
Ecuaciones.ecuacion4()
