from lcapy import *
import sympy as sp

X_z = (-27 / (z - 1/2)) + (9 / (z - 1/2)**2) + (27 / (z + 1/2)) + (18 / (z + 1/2)**2) +  (9/ (z + 1/2)**3)
x_n = X_z(n)
sp.pprint(x_n)



