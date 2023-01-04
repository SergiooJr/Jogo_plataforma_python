import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Sprites')

preto = (0, 0, 0)

# Criando a classe Sapo
class Sapo(pygame.sprite.Sprite): # essa classe Sapo, vai herdar de uma outra classe do pygame, chamada Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # obrigatório
        self.sprites = [] # variável (atributo) que vai armazenar todas as sprites em uma lista
        # armazenando as sprites
        for i in range(1, 11):
            self.sprites.append(pygame.image.load(f'sprites/attack_{i}.png')) # adicionando e carregando as imagens
            # dentro da lista
        self.atual = 0
        self.image = self.sprites[self.atual] # recebe o 1° elemento da nossa lista sprites

        # definindo o tamanho da imagem
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

        # definindo a posição em que a imagem vai aparecer na tela
        self.rect = self.image.get_rect() # pegando o retângulo que fica ao redor da imagem
        self.rect.topleft = 100, 100 # colocando o canto superior esquerdo da imagem a 100px em X, e 100px em Y

# .......................................................ANIMANDO................................................
        self.animar = False
    def atacar(self):
        self.animar = True

    # método herdado da classe sprite
    def update(self):
        if self.animar:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

todas_as_sprites = pygame.sprite.Group()
# instanciando o objeto
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