from lcapy import *
import sympy as sp

X_z = (2*z + 1) / (z**2 + 4*z + 3)
x_n = X_z(n)
sp.pprint(x_n)

print("x[n]")
sp.pprint(x_n.seq((0,10)))
print(f"x[0] = {x_n.evaluate(0)}")
print(f"x[1] = {x_n.evaluate(1)}")
print(f"x[2] = {x_n.evaluate(2)}")

# Versão feita à mão
x2_n = -1/2 * (-1)**(n-1) * u(n-1) + (5/2) * (-3)**(n-1) * u(n-1)
sp.pprint(x2_n)

print("Versão 2 - x[n]")
sp.pprint(x2_n.seq((0,10)))
print(f"x[0] = {x2_n.evaluate(0)}")
print(f"x[1] = {x2_n.evaluate(1)}")
print(f"x[2] = {x2_n.evaluate(2)}")