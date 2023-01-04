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
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip() # melhor que o update