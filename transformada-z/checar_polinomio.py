import sympy as sp
from lcapy import *

# Definir a variável simbólica
x = sp.symbols('z')

# Definir as expressões
#expr1 = (x**3 + x**2 + (3/2)*x + 1/2) / (x**3 + (3/2)*x**2 + (1/2)*x)
#expr2 = 1 + (-x**2 + 2*x + 1) / (2*x**3 + 3*x**2 + x)
#expr3 = 1 - (1/2)*x**(-1) + ((7/4)*x + 3/4) / (x**3 + (3/2)*x**2 + (1/2)*x)

expr1_z = (z**3 + z**2 + (3/2)*z + 1/2) / (z**3 + (3/2)*z**2 + (1/2)*z)
expr2_z = 1 + (-z**2 + 2*z + 1) / (2*z**3 + 3*z**2 + z)
expr3_z = 1 - (1/2)*z**(-1) + ((7/4)*z + 3/4) / (z**3 + (3/2)*z**2 + (1/2)*z)

print("x1[n]")
x1_n = expr1_z(n)
sp.pprint(x1_n)
sp.pprint(x1_n.seq((-10,10)))

print("x2[n]")
x2_n = expr2_z(n)
sp.pprint(x2_n)
sp.pprint(x2_n.seq((-10,10)))

print("x3[n]")
x3_n = expr3_z(n)
sp.pprint(x3_n)
sp.pprint(x3_n.seq((-10,10)))

# Simplificar as expressões
#simplified_expr1 = sp.simplify(expr1)
#simplified_expr2 = sp.simplify(expr2)
#simplified_expr3 = sp.simplify(expr3)

# Verificar se as expressões são equivalentes
#print(simplified_expr1)
#print(simplified_expr2)
#print(simplified_expr3)

# Verificar a equivalência
#is_equal_1_2 = sp.simplify(simplified_expr1 - simplified_expr2) == 0
#is_equal_1_3 = sp.simplify(simplified_expr1 - simplified_expr3) == 0
#is_equal_2_3 = sp.simplify(simplified_expr2 - simplified_expr3) == 0

#print(f"Expr1 == Expr2? {is_equal_1_2}")
#print(f"Expr1 == Expr3? {is_equal_1_3}")
#print(f"Expr1 == Expr3? {is_equal_2_3}")
