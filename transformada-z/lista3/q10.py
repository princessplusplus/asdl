from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Versão Automática")
print("a)")
# X_z = (2*z)/((z-1)*(z+1)), |z| > 1
X_z = (2*z)/((z-1)*(z+1))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=True)
sp.pprint(x_n)

print("\n") 
print("------------------------------------------------")
print("b)")
# X_z = (2*z)/((z-1)*(z+1)), |z| < 1
X_z = (2*z)/((z-1)*(z+1))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=False)
sp.pprint(x_n)

print("\n") 
print("------------------------------------------------")
print("c)")
# X_z = (-2.5*z)/((z-0.5)*(z+2)), |z| > 2
X_z = (-2.5*z)/((z-0.5)*(z+2))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=True)
sp.pprint(x_n)

print("\n") 
print("------------------------------------------------")
print("d)")
# X_z = (-2.5*z)/((z-0.5)*(z+2)), |z| < 0.5
X_z = (-2.5*z)/((z-0.5)*(z+2))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=False)
sp.pprint(x_n)

print("\n") 
print("------------------------------------------------")
print("e)")
# X_z = (-2.5*z)/((z-0.5)*(z+2)), 0.5 < |z| < 2
X_z = (-2.5*z)/((z-0.5)*(z+2))
X_frac = X_z.partfrac()
fractions = X_frac.args  
fraction1, fraction2 = fractions
#sp.pprint(fraction1)
#sp.pprint(fraction2)
X1_z = -2/(z+2)
X2_z = (-1/2)/(z-(1/2))
x1_n = X1_z(n, causal=False)
x2_n = X2_z(n)
x_n = x1_n + x2_n
sp.pprint(x_n)

print("\n") 
print("------------------------------------------------")
print("f)")
# X_z = (z+1)/(z+(1/3)), |z| > 1/3
X_z = (z+1)/(z+(sp.Rational(1, 3)))
x_n = X_z(n)
sp.pprint(x_n.simplify())

print("\n") 
print("------------------------------------------------")
print("g)")
# X_z = (z**2 - 3*z)/(z**2 + (3/2)*z -1), 0.5 < |z| < 2
X_z = (z**2 - 3*z)/(z**2 + (3/2)*z - 1)
X_fat = X_z.factored()
print("Fatorado:")
sp.pprint(X_fat)
print("\n") 
print("Frações parciais:")
X_frac = X_z.partfrac()
sp.pprint(X_frac)
fractions = X_frac.args  
fraction1, fraction2, fraction3 = fractions
#sp.pprint(fraction1)
#sp.pprint(fraction2)
#sp.pprint(fraction3)
X1_z = 1
X2_z = -4/(z+2)
X3_z = (-1/2)/(z-(1/2))
x1_n = delta(n)
x2_n = X2_z(n, causal=False)
x3_n = X3_z(n)
x_n = x1_n + x2_n + x3_n
print("\n") 
print("x[n]:")
sp.pprint(x_n.simplify())

print("\n") 
print("------------------------------------------------")
print("h)")

print("\n") 
print("------------------------------------------------")
print("i)")


time.sleep(20)
os.system('clear')