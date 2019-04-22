# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:18:12 2019

@author: julia
"""

opcoes = cenario_atual['opcoes']
if len(opcoes) == 0:
    print("Fim do jogo")
    game_over = True
else:
    print("Escolha sua opção!")
    for k,v in opcoes.items():
        print()
        if k==" ":
            print("  ")
        else:
            print("{0}:{1}".format(k,v))
               
    print()   
    escolha=input("Qual será a escolha? ")
    if escolha in opcoes:
        nome_cenario_atual = escolha
                