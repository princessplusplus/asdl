from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 5")

h_t = 100 * t * exp(-1*t) * cos(2*t) * u(t)
H_s = h_t(s)

print("H(s)")
#sp.pprint(H_s)

print("\n")

H_fat = H_s.factored()
print("Fatorado:")
sp.pprint(H_fat)

print("\n")


H_jw = H_fat(j * omega)
print("H(jw)")
sp.pprint(H_jw)

print("\n")

#Avaliando em w=2
H_j2 = H_jw.subs(w, 2)
print("H(j2)")
sp.pprint(H_j2)

print("\n")

sp.pprint(H_j2.simplify())

print("\n")

# Modulo
print("Módulo:")
sp.pprint(H_j2.magnitude)

print("\n")

# Fase
print("Fase:")
sp.pprint(H_j2.phase)

print("\n")

x_t = sin(2*t) * u(t)
X_s = x_t(s)

print("X(s)")
#sp.pprint(X_s)

print("\n")

Y_s = H_s * X_s
y_t = Y_s(t)

print("y(t)")
#sp.pprint(y_t)

print("y(t)")
sp.pprint(y_t.simplify())

print("\n")
