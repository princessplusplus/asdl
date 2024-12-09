from lcapy import *
import sympy as sp

#print("Versão Automática")
h_n = delta(n+1) - u(n) + u(n-2)
X_z = z - z**(-2)

#print("H(Z)")
H_z = h_n(z)
#sp.pprint(H_z.expand())

#print("x[n]")
x_n = X_z(n)
#sp.pprint(x_n)

#print("Y(Z)")
Y_z = H_z * X_z
#sp.pprint(Y_z.expand())

#print("y[n]")
y_n = Y_z(n)
#sp.pprint(y_n)

#sp.pprint(y_n.seq((-5,5)))

# Versão (semi) feita à mão
#print("Versão Semi-automática")
x2_z = z - z**(-2)
h2_z = z - (z/(z-1)) + z**(-2) * (z/(z-1))

#print("Y(Z)")
y2_z = x2_z * h2_z
#sp.pprint(y2_z.expand())
y2_n = y2_z(n)
#sp.pprint(y2_n)

#print("Versão 2 - y[n]")
#sp.pprint(y2_n.seq((-5,5)))

# Versão feita à mão
print("Versão Manual")
y3_n = delta(n+2) - u(n+1) + u(n-1) - delta(n-1) + u(n-2) - u(n-4)
#sp.pprint(y3_n)

print("Versão 3 - y[n]")
sp.pprint(y3_n.seq((-5,5)))


# Versão gabarito
print("Versão Gabarito")
y4_n = u(n+2) - 2 * u(n+1) + 2 * u(n-2) - u(n-4)
sp.pprint(y4_n)

print("Versão 4 - y[n]")
sp.pprint(y4_n.seq((-5,5)))