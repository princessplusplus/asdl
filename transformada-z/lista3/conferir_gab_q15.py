from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 15")
print("a)")
print("Gabarito")
x1_n = 10 * (-3)**(n) * u(n) + (3)**(n) * u(n-1)
sp.pprint(x1_n)
print("x[n]:")
sp.pprint(x1_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x2_n = 11 * delta(n) - 30 * (-3)**(n-1) * u(n-1) + 3 * (3)**(n-1) * u(n-1)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(10)
#os.system('clear')

print("b)")
print("Resposta do Professor")
x2_n = (18/2) * n * (n-1) * (-3)**(n-2) * u(n) + 3 * n * (-3)**(n-1) * u(n) + 3 * (-3)**(n) * u(n)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x2_n = 3 * delta(n) - 9 * (3)**(n-1) * u(n-1) + 2 * (-3)**(n-1) * u(n-1) - 1 * n *(-3)**(n-1) * u(n-1) + 1 * n * (n-1) * (-3)**(n-1) * u(n-1)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(1)
#os.system('clear')

print("c)")
print("Gabarito")
x1_n = 50 * (n+1) * (-2)**(n+1) * u(n+1)
sp.pprint(x1_n)
print("x[n]:")
sp.pprint(x1_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x3_n = 100 * ((-2)**(n) * u(n) + n * (-2)**(n-1) * u(n))
sp.pprint(x3_n)
print("x[n]:")
sp.pprint(x3_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(2)
#os.system('clear')

print("d)")
print("Minha resposta")
x2_n = 100 * ((-2)**(n) * u(n) + 1 * n * (-2)**(n-1) * u(n) + 2 * n * (n-1) * (-2)**(n-1) * u(n))
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(3)
#os.system('clear')

print("e)")
print("Gabarito")
x1_n = (sp.Rational(2,3)) * (2)**(n) * u(n) + (sp.Rational(2,9)) * (2)**(n) * u(n) - (sp.Rational(2,9)) * (1/2)**(n) * u(n)
sp.pprint(x1_n)
print("x[n]:")
sp.pprint(x1_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x2_n = (sp.Rational(2,9)) * (2)**(n) * u(n) - (sp.Rational(2,9)) * (1/2)**(n) * u(n)  + (sp.Rational(2,3)) * n * (2)**(n-1) * u(n)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(3)
#os.system('clear')

print("f)")
print("Gabarito")
x1_n = (sp.Rational(1,9)) * (2)**(n) * u(n) - (sp.Rational(4,3)) * (1/2)**(n) * n * u(n) - (sp.Rational(8,9)) * (1/2)**(n) * u(n)
sp.pprint(x1_n)
print("x[n]:")
sp.pprint(x1_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x2_n = (sp.Rational(8,9)) * (1/2)**(n) * u(n) - (sp.Rational(2,3)) * (1/2)**(n-1) * n * u(n) + (sp.Rational(1,9)) * (2)**(n) * u(n)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

#time.sleep(3)
#os.system('clear')
