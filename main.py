from operaciones import *

print(suma(5, 7))
print(resta(10, 6))
print(multiplicacion(7, 5))
print(division(10, 20))
print(division(10, 0))

# importacion completa
import math
print("\n", math.sqrt(16))

# importacion selectiva
from math import sqrt, pow
print("\n", sqrt(16))
print(pow(2, 3))

# importacion con alias
from math import sqrt as raiz
print("\n", raiz(16))

import sys
print("\n", sys.path)