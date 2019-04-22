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