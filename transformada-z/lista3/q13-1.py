import sympy as sp

# Definindo a variável simbólica
z = sp.symbols('z')

# A função dada
numerador = 9
denominador = (z - 1/2)**2 * (z + 1/2)**3

# Expressão completa de X(z)
Xz = numerador / denominador

# Decompondo em frações parciais
frações_parciais = sp.apart(Xz, z)

# Exibindo o resultado
print("Decomposição em frações parciais:")
sp.pprint(frações_parciais)
