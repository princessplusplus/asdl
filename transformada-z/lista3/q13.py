import sympy as sp

# Definindo a variável simbólica
z = sp.symbols('z')
A, B, C, D = sp.symbols('A B C D')

# A função dada
lhs = 9
rhs = ((z - 1/2)**2) * ((z + 1/2)**3))

# A expressão de frações parciais
fractions = (A / (z - 1/2)) + (B / (z - 1/2)**2) + (C / (z + 1/2)) + (D / (z + 1/2)**2) +  (E/ (z + 1/2)**3)

t1 = (z - 1/2)
t2 = (z + 1/2)

tA = A * (t1) * (t2**3)
sp.pprint(tA)
tB = B * (t2**3)
sp.pprint(tA)
tC = C * (t1**2) * (t2)
sp.pprint(tA)
tD = D * (t1**2) * (t2**2)
sp.pprint(tA)
tE = E * (t1)
sp.pprint(tA)

# Expandindo ambos os lados para igualar os coeficientes
lhs_exp = sp.simplify(lhs)
rhs_exp = sp.simplify(rhs)

# Igualando os dois lados
equation = sp.Eq(lhs_exp, rhs_exp)

# Resolvendo a equação para A, B, C e D
coefficients = sp.solve(equation, (A, B, C, D))

# Mostrando os coeficientes
print("Coeficientes de frações parciais:")
for coef, value in coefficients.items():
    print(f"{coef} = {value}")


# A expressão de frações parciais
fractions = (-27 / (z - 1/2)) + (9 / (z - 1/2)**2) + (27 / (z + 1/2)) + (18 / (z + 1/2)**2) +  (9/ (z + 1/2)**3)
