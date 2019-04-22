# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:29:05 2019

@author: julia
"""

import random

n=random.randint(1,21)
print("O mestre comprou uma carta, mas é secreta, tente ganhar! Saiba que é difícil...")
s=0
p=input("Você quer comprar uma carta?  ")
while p=="sim" and s<22:
    x=random.randint(1,13)
    print("você comprou o {0}".format(x))
    s+=x
    print("você está com {0}".format(s))
    if s < 22:
      p=input("Você quer comprar uma carta?  ")
    
if s>n and s<=21:
    print("Você venceu!")
else:
    print("Você perdeu...")
    
