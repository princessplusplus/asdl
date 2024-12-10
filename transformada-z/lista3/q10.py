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
print("x[n]:")
sp.pprint(x_n)
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("b)")
# X_z = (2*z)/((z-1)*(z+1)), |z| < 1
X_z = (2*z)/((z-1)*(z+1))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=False)
print("x[n]:")
sp.pprint(x_n)
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("c)")
# X_z = (-2.5*z)/((z-0.5)*(z+2)), |z| > 2
X_z = (-2.5*z)/((z-0.5)*(z+2))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=True)
print("x[n]:")
sp.pprint(x_n)
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("d)")
# X_z = (-2.5*z)/((z-0.5)*(z+2)), |z| < 0.5
X_z = (-2.5*z)/((z-0.5)*(z+2))
X_frac = X_z.partfrac()
sp.pprint(X_frac)
x_n = X_frac(n, causal=False)
print("x[n]:")
sp.pprint(x_n)
sp.pprint(x_n.seq((-10,10)))

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
print("x[n]:")
sp.pprint(x_n)
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("f)")
# X_z = (z+1)/(z+(1/3)), |z| > 1/3
X_z = (z+1)/(z+(sp.Rational(1, 3)))
x_n = X_z(n)
print("x[n]:")
sp.pprint(x_n.simplify())
sp.pprint(x_n.seq((-10,10)))

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
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("h)")
# X_z = (z**3 + z**2 + (3/2)*z - (1/2))/((z**3 + (3/2)*(z**2) + (1/2)*z)), |z| < 0.5
# Fazer divisão longa de polinômios
X1_z = 1
X2_z = (-1/2) * z**(-1)
X3_z = ((7/4)*z + (3/4))/(z**3 + (3/2)*(z**2) + (1/2)*z) 
X_fat = X3_z.factored(pairs=True)
print("Fatorado:")
sp.pprint(X_fat)
print("\n") 
print("Frações parciais:")
X_frac = X_fat.partfrac()
sp.pprint(X_frac)
fractions = X_frac.args  
fraction1, fraction2, fraction3 = fractions
#sp.pprint(fraction1)
#sp.pprint(fraction2)
#sp.pprint(fraction3)
X31_z = -2/(z+1)
X32_z = (1/2)/(z+(1/2))
X33_z = (3/2)/(z)
x3_n = X31_z + X32_z + X33_z
x_n = delta(n) + X2_z(n) + X31_z(n, causal=False) + X32_z(n) + X33_z(n, causal=False)
sp.pprint(x_n.simplify())
sp.pprint(x_n.seq((-10,10)))

print("\n") 
print("------------------------------------------------")
print("i)")
# X_z = (z**3 + z**2 + (3/2)*z - (1/2))/((z**2 + (3/2)*z + (1/2))), |z| > 1
# Fazer divisão longa de polinômios
X1_z = 1
X2_z = (-1/2)
X3_z = ((7/4)*z + (3/4))/(z**2 + (3/2)*z + (1/2)) 
X_fat = X3_z.factored(pairs=True)
print("Fatorado:")
sp.pprint(X_fat)
print("\n") 
print("Frações parciais:")
X_frac = X_fat.partfrac()
sp.pprint(X_frac)
fractions = X_frac.args  
fraction1, fraction2 = fractions
#sp.pprint(fraction1)
#sp.pprint(fraction2)
X31_z = 2/(z+1)
X32_z = (-1/4)/(z+(1/2))
x3_n = X31_z + X32_z
x_n = delta(n) + X2_z * delta(n) + X31_z(n) + X32_z(n)
sp.pprint(x_n.simplify())
sp.pprint(x_n.seq((-10,10)))

time.sleep(20)
os.system('clear')