from lcapy import *
import sympy as sp

x2_n = -27 * (1/2)**(n-1) * u(n-1) + (9/(1/2)) * (n-1) * (1/2)**(n-1) * u(n-1) + 27 * (-1/2)**(n-1) * u(n-1) + (18/(-1/2)) * (n-1) * (-1/2)**(n-1) * u(n-1) -  36 * (n-1) * (n-2) * (-1/2)**(n) * u(n-1)

# Calcular o somatório de x2_n de n = -infinito até n = +infinito
resultado = sp.summation(x2_n, (n, -sp.oo, sp.oo))
print(resultado)
