from assets.variables import *

def game_over(pontos):
    
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

        bgGameOver = pygame.image.load('assets/fundoGameOver.jpg')
        gameDisplay.blit(bgGameOver, (0, 0))
        pygame.mixer.music.stop()
        
        fonte = pygame.font.Font("freesansbold.ttf", 50)
        fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
        texto = fonte.render(str(pontos) + " pontos!", True, white)
        textoContinue = fonteContinue.render("Pressione enter para reiniciar...", True, white)
        
        gameDisplay.blit(textoContinue, (550, 380))
        gameDisplay.blit(texto, (630, 300))
        pygameDisplay.update()
        clock.tick(30)






def game():

    playing = True
    direcaoCrash = True
    direcaoNitro = True
    velocidade = 10
    pontos = 0

    posXNitro = -250
    posYNitro = random.randrange(0, altura-50)
    posXNitro2 = 0
    posYNitro2 = random.randrange(0, altura-50)
    posXNitro3 = 0
    posYNitro3 = random.randrange(0, altura-50)
    posXNitro4 = 0
    posYNitro4 = random.randrange(0, altura-50)
    posXNitro5 = 0
    posYNitro5 = random.randrange(0, altura-50)
    larguraNitro = 51
    alturaNitro = 50

    posXCrash = 1100
    posYCrash = 350
    larguraCrash = 107
    alturaCrash = 80
    movLeftCrash = 0
    movRightCrash = 0
    movUpCrash = 0
    movDownCrash = 0

    bg = pygame.image.load('assets/fundo.png')
    nitro = pygame.image.load('assets/nitro.png')
    crash = pygame.image.load('assets/crash.png')

    pygame.mixer.music.load('assets/trilha.mp3')
    pygame.mixer.music.play(-1)                                                       #Esse "-1" quer dizer que vai tocar em loop
    pygame.mixer.music.set_volume(1)
    pontoSom = pygame.mixer.Sound('assets/ponto.mp3')
    morte1Som = pygame.mixer.Sound('assets/morte1.mp3')
    morte2Som = pygame.mixer.Sound('assets/morte2.mp3')
 




    while True:                                                                       #Aqui são lidos os eventos da tela
        
        if playing == True:

            for event in gameEvents.get():                                            #Fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:                                      #Quando um botão é pressionado
                    if event.key == pygame.K_a:
                        movLeftCrash = -20
                    elif event.key == pygame.K_d:
                        movRightCrash = 20
                    elif event.key == pygame.K_w:
                        movUpCrash = -20
                    elif event.key == pygame.K_s:
                        movDownCrash = 20

                if event.type == pygame.KEYUP:                                        #Quando um botão é solto
                    if event.key == pygame.K_a:
                        movLeftCrash = 0
                    elif event.key == pygame.K_d:
                        movRightCrash = 0
                    elif event.key == pygame.K_w:
                        movUpCrash = 0
                    elif event.key == pygame.K_s:
                        movDownCrash = 0

                if direcaoCrash == True and movLeftCrash + movRightCrash < 0:         #Fazer o Crash mudar de direção
                    crash = pygame.transform.flip(crash, True, False)
                    direcaoCrash = False
                elif direcaoCrash == False and movRightCrash + movRightCrash > 0:
                    crash = pygame.transform.flip(crash, True, False)
                    direcaoCrash = True

            if posXCrash >= 20:                                                        #Evitar que o Crash saia da tela
                posXCrash = posXCrash + movLeftCrash
            if posXCrash <= largura - 135:
                posXCrash = posXCrash + movRightCrash
            if posYCrash >= 10:
                posYCrash = posYCrash + movUpCrash
            if posYCrash <= altura - 100:
                posYCrash = posYCrash + movDownCrash





            if direcaoNitro == True:                                                  #Comportamento das caixas de Nitro
                if posXNitro < largura:
                    posXNitro = posXNitro + velocidade
                else:
                    direcaoNitro = False
                    pygame.mixer.Sound.play(pontoSom)
                    posYNitro = random.randrange(0, altura-50)
                    pontos = pontos + 1
                    if velocidade < 30:
                        velocidade = velocidade + 1
            else:
                if posXNitro >= -50:
                    posXNitro = posXNitro - velocidade
                else:
                    direcaoNitro = True
                    pygame.mixer.Sound.play(pontoSom)
                    posYNitro = random.randrange(0, altura-50)
                    pontos = pontos + 1
                    if velocidade < 30:
                        velocidade = velocidade + 1
            
            if direcaoNitro == True and pontos >= 30:                                 #Caixas de Nitro 2
                if posXNitro2 < largura:
                    posXNitro2 = posXNitro2 + velocidade
                else:
                    posYNitro2 = random.randrange(0, altura-50)
            elif direcaoNitro == False and pontos >= 30:
                if posXNitro2 >= -50:
                    posXNitro2 = posXNitro2 - velocidade
                else:
                    posYNitro2 = random.randrange(0, altura-50)

            if direcaoNitro == True and pontos >= 40:                                 #Caixas de Nitro 3
                if posXNitro3 < largura:
                    posXNitro3 = posXNitro3 + velocidade
                else:
                    posYNitro3 = random.randrange(0, altura-50)
            elif direcaoNitro == False and pontos >= 40:
                if posXNitro3 >= -50:
                    posXNitro3 = posXNitro3 - velocidade
                else:
                    posYNitro3 = random.randrange(0, altura-50)

            if direcaoNitro == True and pontos >= 50:                                 #Caixas de Nitro 4
                if posXNitro4 < largura:
                    posXNitro4 = posXNitro4 + velocidade
                else:
                    posYNitro4 = random.randrange(0, altura-50)
            elif direcaoNitro == False and pontos >= 50:
                if posXNitro4 >= -50:
                    posXNitro4 = posXNitro4 - velocidade
                else:
                    posYNitro4 = random.randrange(0, altura-50)

            if direcaoNitro == True and pontos >= 60:                                 #Caixas de Nitro 5
                if posXNitro5 < largura:
                    posXNitro5 = posXNitro5 + velocidade
                else:
                    posYNitro5 = random.randrange(0, altura-50)
            elif direcaoNitro == False and pontos >= 60:
                if posXNitro5 >= -70:
                    posXNitro5 = posXNitro5 - velocidade
                else:
                    posYNitro5 = random.randrange(0, altura-50)





            pixelsXCrash = list(range(posXCrash+20, posXCrash + larguraCrash-20))     #Ajustando hitboxes
            pixelsYCrash = list(range(posYCrash+20, posYCrash + alturaCrash+1))
            pixelsXNitro = list(range(posXNitro, posXNitro + larguraNitro+1))
            pixelsYNitro = list(range(posYNitro, posYNitro + alturaNitro+1))

            if len(list(set(pixelsYCrash) & set(pixelsYNitro))) > 0:                  #Detectando colisões
                if len(list(set(pixelsXCrash) & set(pixelsXNitro))) > 0:
                    playing = False
                    pygame.mixer.Sound.play(morte1Som)
                    pygame.mixer.Sound.play(morte2Som)
                    game_over(pontos)





            texto = fonte.render('Pontos: '+str(pontos), True, white)
            
            gameDisplay.blit(bg, (0, 0))                                              #Colocando as coisas na tela
            gameDisplay.blit(nitro, (posXNitro, posYNitro))
            if pontos >= 30:
                gameDisplay.blit(nitro, (posXNitro2, posYNitro2))
            if pontos >= 40:
                gameDisplay.blit(nitro, (posXNitro3, posYNitro3))
            if pontos >= 50:
                gameDisplay.blit(nitro, (posXNitro4, posYNitro4))
            if pontos >= 60:
                gameDisplay.blit(nitro, (posXNitro5, posYNitro5))
            gameDisplay.blit(crash, (posXCrash, posYCrash))    
            gameDisplay.blit(texto, (20, 20))

            pygameDisplay.update()                                                    #Atualizando a tela
            clock.tick(60)

game()