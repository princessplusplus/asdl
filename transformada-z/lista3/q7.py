from lcapy import *
import sympy as sp
import numpy as np
import os
import time

# Definindo a variável simbólica
s = sp.symbols('s')

print("Questão 10")
print("a)")

X_s = 3/(s**2 + 5*s -1)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

print("b)")

X_s = (2 * s**2 + 3)/(s**2 + 5*s +1)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

print("c)")

X_s = (2 * s + 3)/(s**2 + 5*s - 6)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

print("d)")

X_s = (2 * s + 3)/(s**2 + 5*s + 6)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

print("e)")

X_s = ((3 * s**2 + 2 * s)/(s**2 + s - 1))* sp.exp(-5*s)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

print("f)")

X_s = ((3 * s**2 + 2 * s)/(s*(s + 1)*(s+2))) * sp.exp(-3*s)
sX_s = s * X_s

limite_infinito = sp.limit(sX_s, s, sp.oo)
print(f"TVI (x[0]) quando s tende para infinito é: {limite_infinito}")

limite_zero = sp.limit(sX_s, s, 0)
print(f"TVF (x[oo]) quando s tende para 0 é: {limite_zero}")
print("--------------------------------------------")
print("\n") 

time.sleep(10)
os.system('clear')