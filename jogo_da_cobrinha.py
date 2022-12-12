# VÍDEO 08 - pt. 1
from random import randint
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.mixer.music.set_volume(0.3)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1) # com o parâmetro -1 a música fica em looping
barulho_colisao = pygame.mixer.Sound('smw_coin.wav') # tirando a musica de fundo todos os outros arquivos de som
# tem que ser .wav

largura = 640
altura_tela = 480
tela = pygame.display.set_mode((largura, altura_tela))
pygame.display.set_caption('Meu Jogo')
relogio = pygame.time.Clock()

comprimento_quadrado = 20
altura_quadrado = 20

cor_vermelho = (255, 0, 0)
cor_verde = (0, 255, 0)

x_cobra = int((largura/2) - (comprimento_quadrado/2))
y_cobra = int((altura_tela/2) - (altura_quadrado/2))

x_maca = randint(40, 600)
y_maca = randint(50, 430)

x_texto = 420
y_texto = 40
fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, cor_verde, (XeY[0], XeY[1], comprimento_quadrado, altura_quadrado))

while True:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            x_cobra -= 4
        if pygame.key.get_pressed()[K_d]:
            x_cobra += 4
        if pygame.key.get_pressed()[K_w]:
            y_cobra -= 4
        if pygame.key.get_pressed()[K_s]:
            y_cobra += 4
    cobra = pygame.draw.rect(tela, cor_verde, (x_cobra, y_cobra, comprimento_quadrado, altura_quadrado))
    maca = pygame.draw.rect(tela, cor_vermelho, (x_maca, y_maca, comprimento_quadrado, altura_quadrado))
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (x_texto, y_texto))
    pygame.display.update()
