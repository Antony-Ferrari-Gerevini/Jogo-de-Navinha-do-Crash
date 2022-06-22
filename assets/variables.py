import os, time, pygame, random



def inserirDados():

    while True:
        os.system('cls')
        try:
            nome = input('Nome do jogador: ')
            if len(nome) < 2 or len(nome) > 50:
                print('Nome muito longo ou muito curto!')
                raise
            break
        except:
            time.sleep(2)

    while True:
        os.system('cls')
        try:
            arrobaPonto = [0, 0]
            email = str(input('Email: '))
            for i in email:
                if i == '@':
                    arrobaPonto[0] = arrobaPonto[0] + 1
                if arrobaPonto[0] == 1 or i == '.':
                    arrobaPonto[1] = arrobaPonto[1] + 1
            if arrobaPonto[0] != 1:
                raise
            if arrobaPonto[1] < 1:
                raise
            x = email[-1].isalpha()
            if x == False:
                raise
            break
        except:
            print('Email inválido!')
            time.sleep(2)
    
    arquivo = open('Registro.txt','a')
    arquivo.write(f'{nome}: {email}\n')
    arquivo.close()



inserirDados()
pygame.init()
largura = 1480; altura = 800; tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption('Crash')
gameDisplay = pygame.display.set_mode(tamanho)

gameEvents = pygame.event
clock = pygame.time.Clock()
fonte = pygame.font.Font('freesansbold.ttf',30)                                   #Texto informando a pontuação
#fonte = pygame.font.SysFont('Comic Sans MS',30)
white = (255, 255, 255)
#black = (0, 0, 0)

gameIcon = pygame.image.load('assets/crash.png')
pygameDisplay.set_icon(gameIcon)
bg = pygame.image.load('assets/fundo.png')
nitro = pygame.image.load('assets/nitro.png')
crash = pygame.image.load('assets/crash.png')