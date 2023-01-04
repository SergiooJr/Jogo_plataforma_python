import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Sprites')

preto = (0, 0, 0)

class Sapo(pygame.sprite.Sprite): # essa classe sapo, vai herdar de uma outra classe do pygame, chamada Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # obrigatório
        self.sprites = []
        for i in range(1, 11):
            self.sprites.append(pygame.image.load(f'sprites/attack_{i}.png'))

while True:
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.flip() # melhor que o update