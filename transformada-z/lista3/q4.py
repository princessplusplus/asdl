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

H_jw = h_t.as_fourier() 

fase = H_jw.phase
magnitude = H_jw.magnitude

y_t = x_t * magnitude
