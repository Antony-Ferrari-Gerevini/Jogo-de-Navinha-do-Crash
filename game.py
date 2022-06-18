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
    movXCrash = 0
    movYCrash = 0

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
                        movXCrash = -20
                    elif event.key == pygame.K_d:
                        movXCrash = 20
                    elif event.key == pygame.K_w:
                        movYCrash = -20
                    elif event.key == pygame.K_s:
                        movYCrash = 20
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:     #Quando um botão é solto
                        movXCrash = 0
                        movYCrash = 0

            posXCrash = posXCrash + movXCrash
            posYCrash = posYCrash + movYCrash





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