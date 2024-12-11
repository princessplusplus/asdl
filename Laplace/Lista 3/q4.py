from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 4")
print("a)")

h_t = t * exp(-2*t) * u(t)
x_t = 1 + 2 * cos(t) + 3 * cos(2*t) * u(t)

H_s = h_t.as_laplace()
sp.pprint(H_s)

H_jw = h_t.as_fourier() 
sp.pprint(H_jw)

fase = H_jw.phase
print("Fase:")
sp.pprint(fase)
magnitude = H_jw.magnitude
print("Magnitude:")
sp.pprint(magnitude)

y_t = x_t * magnitude
sp.pprint(y_t)
