# # VÍDEO 06 - Gerando Textos
# from random import randint
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# largura = 640
# altura_tela = 480
# tela = pygame.display.set_mode((largura, altura_tela))
# pygame.display.set_caption('Meu Jogo')
# relogio = pygame.time.Clock()
#
# comprimento_retangulo = 40
# altura_retangulo = 50
#
# cor_vermelho = (255, 0, 0)
# cor_azul = (0, 0, 255)
#
# x = (largura/2) - (comprimento_retangulo/2)
# y = (altura_tela/2) - (altura_retangulo/2)
#
# x_azul = randint(40, 600)
# y_azul = randint(50, 430)
#
# x_texto = 420
# y_texto = 40
# # configurando a fonte
# fonte = pygame.font.SysFont('arial', 40, True, True)
#
# pontos = 0
# while True:
#     relogio.tick(30)
#     tela.fill((0, 0, 0))
#     mensagem = f'Pontos: {pontos}'
#     texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if pygame.key.get_pressed()[K_a]:
#             x -= 20
#         if pygame.key.get_pressed()[K_d]:
#             x += 20
#         if pygame.key.get_pressed()[K_w]:
#             y -= 20
#         if pygame.key.get_pressed()[K_s]:
#             y += 20
#     ret_vermelho = pygame.draw.rect(tela, cor_vermelho, (x, y, comprimento_retangulo, altura_retangulo))
#     ret_azul = pygame.draw.rect(tela, cor_azul, (x_azul, y_azul, comprimento_retangulo, altura_retangulo))
#     if ret_vermelho.colliderect(ret_azul):
#         x_azul = randint(40, 600)
#         y_azul = randint(50, 430)
#         pontos += 1
#     tela.blit(texto_formatado, (x_texto, y_texto))
#     pygame.display.update()



# VÍDEO 07 - Música e Som
from random import randint
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura_tela = 480
tela = pygame.display.set_mode((largura, altura_tela))
pygame.display.set_caption('Meu Jogo')
relogio = pygame.time.Clock()

comprimento_retangulo = 40
altura_retangulo = 50

cor_vermelho = (255, 0, 0)
cor_azul = (0, 0, 255)

x = (largura/2) - (comprimento_retangulo/2)
y = (altura_tela/2) - (altura_retangulo/2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

x_texto = 420
y_texto = 40
fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            x -= 20
        if pygame.key.get_pressed()[K_d]:
            x += 20
        if pygame.key.get_pressed()[K_w]:
            y -= 20
        if pygame.key.get_pressed()[K_s]:
            y += 20
    ret_vermelho = pygame.draw.rect(tela, cor_vermelho, (x, y, comprimento_retangulo, altura_retangulo))
    ret_azul = pygame.draw.rect(tela, cor_azul, (x_azul, y_azul, comprimento_retangulo, altura_retangulo))
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
    tela.blit(texto_formatado, (x_texto, y_texto))
    pygame.display.update()