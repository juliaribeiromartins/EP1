hitus=100
atus=20
if nome_cenario_atual=="lutar":
   hitpc=100
   atpc=5
   print("você possui {0} hit points e {1} de ataque".format(hitus,atus))
   print("O inimigo possui {0} hit points e {1} de ataque".format(hitpc,atpc))
                    
   while hitpc>0:
         hitpc-=atus
         hitus-=atpc
         print("Você derrotou o inimigo! Ainda possui {0} hit points".format(hitus))
         nome_cenario_atual="lutar"
                    
                    
         
                    
if nome_cenario_atual=="jogar a partida":
    atapc2=10
    hitpc2=50
    print("você possui {0} hit points e {1} de ataque".format(hitus,atus))
    print("O inimigo possui {0} hit points e {1} de ataque".format(hitpc2,atapc2))
                     
    while hitpc2>0:
        hitpc2-=atus
        hitus-=atapc2
    print("Você derrotou o inimigo! Ainda possui {0} hit points".format(hitus))
    nome_cenario_atual="jogar a partida"
     

           
          
if nome_cenario_atual=="fuga":
    a=random.randint(1,3)
    b=int(input("Escolha um número de 1 a 3:"))
    if b==a:
        print("Você conseguiu pegar o pen drive")
        nome_cenario_atual="fuga"
    else:
        print("O veterano descobriu e devorou a sua alma")
        print("Fim de Jogo")
        game_over=True
                        