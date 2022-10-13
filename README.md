<h1 align="center">Ecuaciones diferenciales</h1>

En este [repositorio](https://github.com/Diegodesantos1/Ecuaciones_diferenciales) queda resuelto el ejercicio de ecuaciones diferenciales

***

![image](https://user-images.githubusercontent.com/91721855/195686741-c972b402-ae6c-4ad3-9271-7fd7e4cd2493.png)

El código empleado es el siguiente:

```python
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
```
