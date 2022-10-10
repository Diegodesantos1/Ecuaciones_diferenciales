import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class Ecuaciones_diferenciales:
    def ecuacion4():
        t = sp.Symbol('t') ; y = sp.Function('y')
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        print(f" La solución es {sp.dsolve(ecuacion, y(t))}")



Ecuaciones_diferenciales.ecuacion1()
