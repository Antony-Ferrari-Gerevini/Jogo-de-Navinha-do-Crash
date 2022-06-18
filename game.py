from assets.variables import *





def game():

    playing = True
    direcaoCrash = True
    direcaoNitro = True
    velocidade = 10
    pontos = 0

    posXNitro = -250
    posYNitro = random.randrange(0, altura-50)

    posXCrash = 1100
    posYCrash = 350
    movLeftCrash = 0
    movRightCrash = 0
    movUpCrash = 0
    movDownCrash = 0

    bg = pygame.image.load('assets/fundo.png')
    nitro = pygame.image.load('assets/nitro.png')
    crash = pygame.image.load('assets/crash.png')
 




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
                    posYNitro = random.randrange(0, altura-50)
                    pontos = pontos + 1
                    if velocidade < 30:
                        velocidade = velocidade + 1
            else:
                if posXNitro >= -50:
                    posXNitro = posXNitro - velocidade
                else:
                    direcaoNitro = True
                    posYNitro = random.randrange(0, altura-50)
                    pontos = pontos + 1
                    velocidade = velocidade + 1





            texto = fonte.render('Pontos: '+str(pontos), True, white)
            
            gameDisplay.blit(bg, (0, 0))                                              #Colocando as coisas na tela
            gameDisplay.blit(nitro, (posXNitro, posYNitro))
            gameDisplay.blit(crash, (posXCrash, posYCrash))    
            gameDisplay.blit(texto, (20, 20))

            pygameDisplay.update()                                                    #Atualizando a tela
            clock.tick(60)

game()