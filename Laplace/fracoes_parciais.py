from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 3")

#y_t = -1 * (sp.Rational(2,3)) * exp(2*t) * u(-t) + (sp.Rational(1,3)) * exp(-1*t) * u(t)
y_t = (sp.Rational(2,3)) * exp(2*t) * u(t) + (sp.Rational(1,3)) * exp(-1*t) * u(t)
Y_s = y_t(s)
print("Y(s)")
sp.pprint(Y_s)

print("\n")

Y_fat = Y_s.factored()
print("Fatorado:")
sp.pprint(Y_fat)

print("\n")

Y_frac = Y_fat.partfrac()
print("Frações parciais:")
sp.pprint(Y_frac)

print("\n")

X_s = (s+2)/(s-2)
print("X(s)")
sp.pprint(X_s)
H_s = Y_s / X_s

print("\n")

print("H(s)")
sp.pprint(H_s.simplify())

print("\n")

h_t = H_s(t)
H_fat = H_s.factored()
print("Fatorado:")
sp.pprint(H_fat)

print("\n")

H_frac = H_fat.partfrac()
print("Frações parciais:")
sp.pprint(H_frac)

print("\n")

print("h(t)")
sp.pprint(h_t)

Y_s_check = - (sp.Rational(1,3)) * (s/(s-2)*(s+1))
y_t_check = Y_s_check(t)
#sp.pprint(y_t_check)


time.sleep(36)
os.system('clear')