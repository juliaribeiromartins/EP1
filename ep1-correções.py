# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:42:04 2019

@author: julia
"""

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "fumódromo",
            "descricao": "Você acabou de descer do Uber, oque fazer agora?",
            "opcoes": {
                "predio 2": " Tentar achar o professor no prédio novo",
                "entrada p1": " Adentrar o saguão de entrada"
            }
        },
        "predio 2": {
            "titulo": "Entrada prédio novo ",
            "descricao": "Ops... o prédio está fechado!",
            "opcoes": {
                "entrada p1": "Adentrar o sagão de entrada do prédio 1"
            }
        },
        "entrada p1": {
            "titulo": "Sagão de entrada do Inpser",
            "descricao": "Você como brilhante e preguiçoso aluno que é resolve ir na sala dos professores em busca de Raul.",
            "opcoes": {
                "elevador":"vale a pena gastar seus minutos preciosos?",
                "escadas":"pode ser mais rápido, mas pode ser perigoso, tem certeza?"
            }
        },
        "escadas": {
            "titulo": "escadaria do terror",
            "descricao": "Você acaba de fazer uma escolha errada, encontrou um veterano em semana de prova",
            "opcoes": {
                "lutar":"comate com um veterano nervoso",
                "fugir":"é uma decisão bem arriscada"
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
            "descricao": " Você chegou na sala e descobriu que estava vazia, e do nada surgiu um palhaço!"
            "Ui, que susto!"
            "que perda de tempo!",
            "opcoes": {"biblioteca": " ir para a biblioteca"}
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
            "descricao": "Você arriscou jogar com o veterano e.....Ganhou!"
             " Porém, nâo tinha prêmio nenhum ha ha ha",
            "opcoes": {
                "help desk":"eles sempre ajudam não é mesmo?",
                "sala de aula":"quem sabe não está com algum professor "
            }
        },
        "help desk": {
            "titulo": "hospital do pc",
            "descricao": "Que sorte!, o primeiro dos pen drives estava dando sopa," 
            "aproveite e guarde.",
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
            "mas, terá que batalhar com o veterano no mario kart",
            "opcoes": {"quadra": " em busca do último pen drive"
                      
                       
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
          "sala dos supercomputadores": {
            "titulo": "o encontro final",
            "descricao": " Parabéns! Você concectou os três pen drives, salvando o Raul,"
            " e ainda deu o doce do elevador pra ele!"
            "Mas será que isso foi o suficiente para o adiamento do EP?",
            "opcoes": {}
      },
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
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
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Escolha sua opção!")
            for k,v in opcoes.items():
               print()
               print("{0}:{1}".format(k,v))
            print()   
            escolha=input("Qual será a escolha? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
                if nome_cenario_atual=="jogar":
                   import random
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
                       nome_cenario_atual= "jogar"
                   else:
                       print("Voce perdeu") 
                       #game_over=True
                if nome_cenario_atual=="elevador":
                       inventario.append("chocolate")
                if nome_cenario_atual=="lutar":
                    
                    hitus=100
                    hitpc=100
                    atus=20
                    atpc=5
                    print("Você possui {0} hit points e {1} de ataque".format(hitus,atus))
                    print("O inimigo possui{0} hit points e {1} de ataque".format(hitpc,atpc))   
                    
                    while hitpc>0:
                        hitpc-=atus
                        hitus-=atpc
                    print("Você derrotou o inimigo! Ainda possui {0} hit points".format(hitus))
                    print("Você conseguiu!")
                    print("_______________")
                    print("Agora que você conseguiu vencer a batalha, continue a busca pelo Raul!")
                    print()       
                            
                 
                       
            else:
                game_over = True

            print("Putzzzz, não foi dessa vez! Parece que alguém ficou de DP...")


if __name__ == "__main__":
    main()