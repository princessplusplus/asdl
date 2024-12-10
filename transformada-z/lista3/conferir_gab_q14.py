from lcapy import *
import sympy as sp
import numpy as np
import os
import time

print("Questão 14")
print("a)")
print("Gabarito")
x1_n = -u(n) - (-1)**(n) * u(n)
sp.pprint(x1_n)
print("x[n]:")
sp.pprint(x1_n.seq((-10,10)))
print("\n") 
print("***")
print("\n") 
print("Minha resposta")
x2_n = -u(n) - (-1)**(n) * u(n)
sp.pprint(x2_n)
print("x[n]:")
sp.pprint(x2_n.seq((-10,10)))
print("--------------------------------------------")
print("\n") 

time.sleep(3)
os.system('clear')


