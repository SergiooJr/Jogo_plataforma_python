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

largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Meu Jogo')
relogio = pygame.time.Clock()

comprimento_quadrado = 20
altura_quadrado = 20

cor_vermelho = (255, 0, 0)
cor_verde = (0, 255, 0)

x_cobra = int((largura_tela/2) - (comprimento_quadrado/2))
y_cobra = int((altura_tela/2) - (altura_quadrado/2))

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

x_texto = 420
y_texto = 40
fonte = pygame.font.SysFont('arial', 40, True, True)
fonte2 = pygame.font.SysFont('arial', 22, True, True)

pontos = 0

lista_cobra = []
comprimento_inicial = 5

morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, cor_verde, (XeY[0], XeY[1], comprimento_quadrado, altura_quadrado))

def reiniciar_jogo():
    global pontos, comprimento_inicial, lista_cobra, lista_cabeca, x_cobra, y_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    lista_cobra = []
    lista_cabeca = []
    x_cobra = int((largura_tela / 2) - (comprimento_quadrado / 2))
    y_cobra = int((altura_tela / 2) - (altura_quadrado / 2))
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # fazendo a cobra se movimentar sem parar
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = -velocidade
                y_controle = 0
            if event.key == K_d and x_controle != -velocidade:
                x_controle = velocidade
                y_controle = 0
            if event.key == K_w and y_controle != velocidade:
                y_controle = -velocidade
                x_controle = 0
            if event.key == K_s and y_controle != -velocidade:
                y_controle = velocidade
                x_controle = 0
    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela, cor_verde, (x_cobra, y_cobra, comprimento_quadrado, altura_quadrado))
    maca = pygame.draw.rect(tela, cor_vermelho, (x_maca, y_maca, comprimento_quadrado, altura_quadrado))

    # recebe x, y da posição atual da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    # recebe x, y de todas as posições já assumidas pela cobra
    lista_cobra.append(lista_cabeca)
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

        # o que faz a cobra crescer
        comprimento_inicial += 1

    # condição para a cobra não crescer desordenadamente
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))

            # mensagem de game over
            mensagem = f'VOCÊ MORREU! Aperte a tecla R para recomeçar.'
            texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
            ret_texto = texto_formatado.get_rect()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura_tela//2, altura_tela//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    # fazendo a cobra paracer do outro lado caso ela vaze da tela
    if x_cobra > largura_tela:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura_tela
    if y_cobra > altura_tela:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura_tela

    # isso é para que armazenemos apenas os valores que a cobra já assumiu, porém de acordo com seu tamanho
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (x_texto, y_texto))
    pygame.display.update()
