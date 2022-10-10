import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math
class Ecuaciones:
    def ecuacion1():
        x = sp.Symbol("x") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(x), (x**2 - 1)/(1 + 1/y(x)))
        ics = {y(3): -1}
        print(f" La solución de la primera ecuación es {sp.dsolve(ecuacion, y(x), ics=ics)}")
    def ecuacion2():
        t = sp.Symbol("t") ; y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) * sp.sin(t), y(t) * sp.log(y(t)))
        ics = {y((math.pi/2)): math.e}
        print(f" La solución de la segunda ecuación es {sp.dsolve(ecuacion, y(t), ics=ics)}")
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
