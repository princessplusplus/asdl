import sympy as sp

# Definindo a variável n
n = sp.symbols('n')

# Definindo a função Heaviside para u(n-1)
u = sp.Heaviside(n - 1)

# Definindo a expressão de x2_n sem depender de 'lcapy'
x2_n = -27 * (1/2)**(n-1) * u + (9/(1/2)) * (n-1) * (1/2)**(n-1) * u + \
       27 * (-1/2)**(n-1) * u + (18/(-1/2)) * (n-1) * (-1/2)**(n-1) * u - \
       36 * (n-1) * (n-2) * (-1/2)**(n) * u

# Calculando a soma numericamente até n = 1000
resultado_num = sum([x2_n.subs(n, i) for i in range(0, 2001)])

# Simplificando o resultado como uma fração
resultado_simplificado = sp.simplify(resultado_num)

# Imprimindo o resultado
print(f"c) Somatório [-inf, +inf]:", resultado_simplificado)