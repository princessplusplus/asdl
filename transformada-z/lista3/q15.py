from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 15 (B)")

Y_z = (-108 * z)/((z+3)**3 * (z-3))
y_n = Y_z(n)
print("y[n]")
sp.pprint(y_n)

print("\n")

Y_fat = Y_z.factored()
print("Fatorado:")
sp.pprint(Y_fat)

print("\n")

Y_frac = Y_fat.partfrac()
print("Frações parciais:")
sp.pprint(Y_frac)





time.sleep(36)
os.system('clear')