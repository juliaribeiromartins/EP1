# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:49:44 2019

@author: julia
"""

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "fumodromo",
            "descricao": "acabou de descer do Uber, oque fazer agora?",
            "opcoes": {
                "Prédio 2": "Tentar achar o professor no prédio novo",
                "Entrar sagão P1": "Adentrar o sagão de entrada"
            }
        },
        "predio 2": {
            "titulo": "Entrada prédio novo ",
            "descricao": "Ops... o prédio está fechado!",
            "opcoes": {
                "Entrada P1": "Adentrar o sagão de entrada do prédio 1"
            }
        },
        "sagão entrada": {
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
            "descricao": "__ acabou de entrar no elevador, e encontrou o doce preferido do Raul, é melhor guardar, pode ser útil no futuro!",
            "opcoes": {
                "sala dos professores": "Você chegou. Ir até a sala dos professores"
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
            "descricao": " Você chegou na sala e descobriu que estava vazia,"
            "que perda de tempo!",
            "opcoes": {"biblioteca": " ir para a biblioteca"}
        },
        "biblioteca": {
            "titulo": "Sala da enrolação",
            "descricao": "Voce esta na biblioteca e terá que jogar um jogo de cartas com seu veterano",
            "opcoes": {
                "jogar": "jogar com o veterano"
            }
        },
            "jogar": {
            "titulo": "21",
            "descricao": "Você arriscou jogar com o veterano e.....Ganhou!"
             " Porém, nâo tinha prêmio nenhum ha ha ha",
            "opcoes": {
                "Help desk":"eles sempre ajudam não é mesmo?",
                "sala de aula":"quem sabe não está com algum professor "
            }
        },
        "Help Desk": {
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
                "Help desk": "continue procurando o pen drive",
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








 
