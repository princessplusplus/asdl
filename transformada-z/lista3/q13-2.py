from lcapy import *
import sympy as sp

X_z = (-27 / (z - 1/2)) + (9 / (z - 1/2)**2) + (27 / (z + 1/2)) + (18 / (z + 1/2)**2) +  (9/ (z + 1/2)**3)
x_n = X_z(n)
sp.pprint(x_n)

print("x[n]")
sp.pprint(x_n.seq((0,20)))
print(f"x[0] = {x_n.evaluate(0)}")
print(f"x[4] = {x_n.evaluate(4)}")
print(f"x[5] = {x_n.evaluate(5)}")

# Versão feita à mão
x2_n = -27 * (1/2)**(n-1) * u(n-1) + (9/(1/2)) * (n-1) * (1/2)**(n-1) * u(n-1) + 27 * (-1/2)**(n-1) * u(n-1) + (18/(-1/2)) * (n-1) * (-1/2)**(n-1) * u(n-1) -  36 * (n-1) * (n-2) * (-1/2)**(n) * u(n-1)
sp.pprint(x2_n)

print("Versão 2 - x[n]")
sp.pprint(x2_n.seq((0,20)))
print(f"x[0] = {x2_n.evaluate(0)}")
print(f"x[4] = {x2_n.evaluate(4)}")
print(f"x[5] = {x2_n.evaluate(5)}")