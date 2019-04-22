# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:18:48 2019

@author: julia
"""

import random
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "fumódromo",
            "descricao": "Você acabou de descer do Uber, o que fazer agora?",
            "opcoes": {
                "predio 2": " Tentar achar o professor no prédio novo",
                "entrada p1": " Adentrar o saguão de entrada"
            }
        },
        "predio 2": {
            "titulo": "Entrada prédio novo ",
            "descricao": "Ops... o prédio está fechado!",
            "opcoes": {
                "entrada p1": "Adentrar o saguão de entrada do prédio 1"
            }
        },
        "entrada p1": {
            "titulo": "Saguão de entrada do Inpser",
            "descricao": "Você como brilhante e preguiçoso aluno que é resolve ir na sala dos professores em busca de Raul.",
            "opcoes": {
                "elevador":"vale a pena gastar seus minutos preciosos?",
                "escadas":"pode ser mais rápido, mas perigoso, tem certeza?"
            }
        },
        "escadas": {
            "titulo": "escadaria do terror",
            "descricao": "Você acaba de fazer uma escolha errada, encontrou um veterano em semana de prova",
            "opcoes": {
                "lutar":"combate com um veterano nervoso",
                
            }
        },
            "lutar": {
            "titulo": "Você conseguiu!",
            "descricao": "Agora que você conseguiu vencer a batalha, continue a busca pelo Raul",
            "opcoes": {
                "sala dos professores":"Ir até a sala dos professores",
                
            }
        },
            
        "elevador": {
            "titulo": "cápsula da velocidade",
            "descricao": "Você acabou de entrar no elevador, e encontrou o doce preferido do Raul, que agora esta no seu inventário porque pode ser útil no futuro!",
            "opcoes": {
                "sala dos professores": " Ir até a sala dos professores"
            }
        },
        "sala dos professores": {
            "titulo": "sala onde habitam os mestres",
            "descricao": "Você chegou na sala dos professores, mas o Raul não está aqui."
            "No lugar há uma carta de um vírus malígno dizendo que sequestrou ele."
            "Para salvá-lo encontre os três pen drives que estão espalhados pelo Insper,"
            "e leve-os até a sala de supercomputadores que está localizada no prédio 2.",
            "opcoes": {
                "biblioteca": "Ir para a biblioteca e tentar pedir ajuda",
                "nerd box": " ir para a nerd box"
            }
        },
        "nerd box": {
            "titulo": "Sala do silêncio profundo",
            "descricao": " Você chegou na sala e descobriu que estava vazia!"
            "que perda de tempo!",
            "opcoes": {"biblioteca": " ir para a biblioteca",
                        " ": " "
            }
        },
        "biblioteca": {
            "titulo": "Sala da enrolação",
            "descricao": "Voce está na biblioteca e terá que jogar um jogo de cartas com seu veterano",
            "opcoes": {
                "jogar": "jogar com o veterano"
            }
        },
            "jogar": {
            "titulo": "21",
            "descricao": "O veterano lhe parabenizou pela boa partida",
            "opcoes": {
                "help desk":"eles sempre ajudam não é mesmo?",
                "sala de aula":"quem sabe não está com algum professor "
            }
        },
            
        "help desk": {
            "titulo": "hospital do pc",
            "descricao": "Que sorte!, o primeiro dos pen drives estava dando sopa," 
            "ele já está guradado no seu inventário.",
            "opcoes": {
                "sala de aula": "ir para a sala de aula",
                "sala do wii": " ir para sala do wii"
            }
        },
        "sala de aula": {
            "titulo": "sala Sebastião Camargo",
            "descricao": "Você chegou na sala de aula, e atrapalhou o pelicano!",
            "opcoes": {
                "help desk": "continue procurando o pen drive",
                "biblioteca": " voltar na biblioteca"
            }
        },
        "sala do wii": {
            "titulo": "toca dos veteranos",
            "descricao": " Você chegou na sala e descobriu que tem outro pen drive aqui,"
            "mas, terá que batalhar com o veterano no quizz",
            "opcoes": {"quizz": " em busca do último pen drive"
                      
                       
           }
        },
          "quizz": {
            "titulo": "Espero que tenha gostado do quizz!",
            "descricao": "Agora que você já fez o quizz, um pen drive sera guardado no seu inventario",
            "opcoes": {"quadra": " esta chegando a batalha final",
                       
                      
           }
        },
          "quadra": {
            "titulo": "ringue de batalha",
            "descricao": "Está na hora da sua batalha final"
            "para conseguir o último dos pen drives, você deverá jogar basquete com um monstro da atlética" ,
            "opcoes": {"jogar a partida": " ganhar honestamente",
                       "fuga": " pegar o pen drive sem que o veterano perceba"
                      
           }
        },
          "jogar a partida": {
            "titulo": "let's go.",
            "descricao": "Você jogou mais uma partida e ganhou o último dos pen drives" ,
            "opcoes": {"sala dos supercomputadores": "tentar salvar o Raul"
                      
           }
        },
           "fuga": {
            "titulo": "corree!!!",
            "descricao": "Você conseguiu o pen drive!",
            "opcoes": {"sala dos supercomputadores": "tentar salvar o Raul"
                      
           }
        },
          "sala dos supercomputadores": {
            "titulo": "o encontro final",
            "descricao": " Parabéns! Você concectou os três pen drives, salvando o Raul,"
            " e ainda deu o doce do elevador pra ele!"
            "Como forma de agradecimento o Raul decidiu te dar um adiantamento... Que sorte hein?",
            "opcoes": {}
      },
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Fugindo da DP!")
    print("--------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()


    cenarios, nome_cenario_atual = carregar_cenarios()
    inventario=[]
    game_over = False
    
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual['titulo'])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual['descricao'])

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
                        
                if nome_cenario_atual==" ":
                   x=random.randint(1,3)
                   y=int(input("Você chegou ao covil do silêncio desesperador,"
                           "um ser ancestral esta lhe propondo uma viagem "
                           "épica entre dimensões, mas para isso, você deve "
                           "acertar um número entre 1 e 3, é fácil vai! Digite o número:"))
                   if x==y:
                       print("Voce foi teletransportado para a terrivel Ronanodax, "
                             "la tudo é escuro e sombrio..."
                             "Depois de muito tempo explorando as áreas voce chega "
                             "a uma sala extremamente secreta dentro da dimensão super secreta "
                             "e avista o que parece ser o rei daquele mundo sombrio... "
                             "O QUEEEEE, HUMBERTOO!!!! Lá estava ele, acariciando sua besta "
                             "aterrorizante do submundo que tinha como nome Floquinho. Depois de muito "
                             "conversar sobre receitas de doce e energia eólica ele resolve "
                             "mandar voce de volta para terra.") 
                   else:
                       print ('')
                       print("Voce acabou de perder um oportunidade unica") 
                   
                   nome_cenario_atual= "nerd box"
                        
                        
                        
                        
                        
                   
    
   
                if nome_cenario_atual=="jogar":
                    
                    
                    n=random.randint(1,21)
                    print("O mestre comprou uma carta, mas é secreta. Tente ganhar, mas saiba que é difícil")
                    s=0
                    p=input("Você quer comprar uma carta?")
                    while p=="sim"and s<22:
                        
                        x=random.randint(1,13)
                        print("você comprou o {0}".format(x))
                        s+=x
                        print("voce esta com {0}".format(s))
                        if s<22:
                            
                            p=input("você quer comprar uma carta?")
                    if s>n and s<=21:
                        
                        print("Você venceu")
                    
                    else:
                        
                        hitus=55

                        print("Você Perdeu o jogo, e, junto,20 hit points!Ainda possui {0} hit points".format(hitus))
                    nome_cenario_atual= "jogar"
                       
                if nome_cenario_atual=="quizz": 
                    print("Responta todas as perguntas seguintes com apenas sim ou nao.")
                    print("____________________")


                    a=input("A Watson,inteligência artificial da IBM, já atuou na culinária?  ")
                    if a=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
    
                    b=input("Já existe uma robô, primeira inteligência artificial, a ter uma documentação de cidadania?  ")
                    if b=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
    
                    c=input("Em 1950 a Inteligência Artificial já tinha sido considerada um um campo de estudo?  ")
                    if c=="nao":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")

                    d=input("As tecnologias que são acopladas a roupas e peças de vestuário são chamadas de wearble?  ")
                    if d=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
                    d=input("Raul tem Facebook?  ")
                    if d=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Procure direito, você vai achar!")
                    nome_cenario_atual= "quizz"
                
                if nome_cenario_atual=="sala dos supercomputadores":
                   v="sala dos supercomputadores"
                   c=input("Para se teletransportar você de saber o nome da sala que deve ir. Dica:"
                            "A sala tem um computador super-herói! Digite o nome da sala:")
                   tele=True
                   while tele:
                       if v==c:
                           print("Finalmente, finalmente você chegou ao estágio final, o grande chefão o aguarda e a preocupação com a segurança do seu professor"
                               " é a única coisa que lhe importa. Você vai até o supercomputador e o vírus maligno tenta manter você distante do mesmo através"
                               " de ondas de choque, mas você tem a benção dos pendrives sagrados, nosso herói alcança o painel do computador e introduz os "
                               " pendrives para conferir o seu conteúdo, ali estava, a salvação para o professor Raul estava o tempo todo dentro dos pendrives."
                               " cada um deles carregava parte de um antivírus místico extremamente potente! Você consegue escutar o vírus com seus gritos de ódio"
                                " e dor através das caixas de som. Uma luz forte lhe ofusca e finalmente o objetivo de nossa jornada foi alcançada, la estava ele "
                                " o inconfundível professor Raul!") 
                           tele=False
                       else:
                           c=input("tente novamente:")
                 
                   nome_cenario_atual= "sala dos supercomputadores"
                      
                elif nome_cenario_atual=="elevador":
                    inventario.append("doce")
                elif nome_cenario_atual=="help desk" or  nome_cenario_atual=="sala do wii" or  nome_cenario_atual=="quadra":
                    inventario.append("pen drive")
                
                            
                 
                       
            else:
                game_over = True


if __name__ == "__main__":
    main()