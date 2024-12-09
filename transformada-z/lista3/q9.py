from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Versão Automática")
print("a)")
# x_n = u(-n)
X_z = (z**(-1))/((z**(-1)) -1)
x_n = X_z(n)
sp.pprint(X_z.factored())

print("------------------------------------------------")
print("b)")
# x[n] = (2)ˆ(-n) * u(n) convolução (3)ˆ(-n) * u(n)
x1_n = (2)**(-n) * u(n)
x2_n = (3)**(-n) * u(n)
X1_z = x1_n(z) 
X2_z = x2_n(z)
#Convolução no tempo --> multiplicação na frequência
X_z = X1_z * X2_z
sp.pprint(X_z.factored())

print("------------------------------------------------")
print("c)")
# x[n] = n * [(2)ˆ(-n) * u(n) convolução (2)ˆ(-n) * u(n)]
x1_n = (2)**(-n) * u(n)
x2_n = (2)**(-n) * u(n)
X1_z = x1_n(z) 
X2_z = x2_n(z)
#Convolução no tempo --> multiplicação na frequência
X_z = X1_z * X2_z
# n no tempo --> derivada em z na frequência (-z * d/dz X(z))
Xd_z = sp.diff(X_z, z)
Xf_z = -z * Xd_z
sp.pprint(Xf_z.factored())

print("------------------------------------------------")
print("d)")
# x[n] = (3)**(n) * cos(2 * n)**2 * u(n)
# cos(2n)**2 = 1/2(1 + cos(4n))
# x_n = (3)**(n) * ((1/2) * (1 + cos(4*n))) * u(n)
x1_n = (3)**(n) * 1 * u(n)
X1_z = x1_n(z)
# x2_n = (3)**(n) * (1/2) * cos(4*n) * u(n)
x2_n = cos(4*n) * u(n)
X2_z = x2_n(z)
X3_z = X2_z.subs(z, z / 3)
X_z = x1_n(z) + X3_z
sp.pprint((1/2) *(X1_z.factored() + X3_z.general()))

print("------------------------------------------------")
print("e)")
# x[n] = (2)**(n) * sen(3 * n)**2 * u(n)
# sen(2n)**2 = 1/2(1 - cos(6n))
# x_n = (2)**(n) * ((1/2) * (1 - cos(6*n))) * u(n)
x1_n = (2)**(n) * 1 * u(n)
X1_z = x1_n(z)
# x2_n = (2)**(n) * (1/2) * cos(6*n) * u(n)
x2_n = cos(6*n) * u(n)
X2_z = x2_n(z)
X3_z = X2_z.subs(z, z / 2)
X_z = x1_n(z) + X3_z
sp.pprint((1/2) *(X1_z.factored() - X3_z.general()))

print("------------------------------------------------")
print("f)")
# x[n] = sen(pi/8 * n - pi/4)**2 * u(n-2)
# x_n = sin(pi/8 * n - pi/4)**2 * u(n-2)
# É necessário ajustar para que tudo esteja com o mesmo delocamento
# x_n = sin(pi/8 * (n-2+2) - pi/4)**2 * u(n-2)
# x_n = sin(pi/8 * (n-2) + 2pi/8 - pi/4)**2 * u(n-2)
# x_n = sin(pi/8 * (n-2) + 1pi/4 - pi/4)**2 * u(n-2)
# x_n = sin(pi/8 * (n-2))**2 * u(n-2)
# Com a propriedade do deslocamento no tempo
# x[n - n0] <-----> z**(-n0) * X(z)
# Então podemos considerar X(z) = sin(pi/8 * n)**2 * u(n)
# e depois Xf_z = z**(-2) * X(z)
pi_8 = symbols('pi/8')
x1_n = sin(pi_8*n) * u(n)
X1_z = x1_n(z)
sp.pprint(z**(-2) * (X1_z.general()))

print("------------------------------------------------")
print("g)")
# x[n] = n * sen(pi/2 * n) * u(-n)
# x1[n] = sen(pi/2 * n) * u(n)
pi_2 = symbols('pi/2')
x1_n = sin(pi/2 * n) * u(n)
X1_z = x1_n(z) 
# n no tempo --> derivada em z na frequência (-z * d/dz X(z))
Xd_z = sp.diff(X1_z, z)
Xf_z = -z * Xd_z
sp.pprint(Xf_z.general())

time.sleep(20)
os.system('clear')