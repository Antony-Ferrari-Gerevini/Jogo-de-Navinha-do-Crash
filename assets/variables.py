import pygame, random

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

bg = pygame.image.load('assets/fundo.png')
nitro = pygame.image.load('assets/nitro.png')
crash = pygame.image.load('assets/crash.png')
