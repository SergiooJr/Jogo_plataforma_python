# VÍDEO 01 - Criando janela
# import pygame
# from pygame.locals import *
# from sys import exit
#
# # inicializando todas as bibliotecas e variáveis da biblioteca pygame
# pygame.init()
#
# # criando janela
# largura = 640
# altura = 480
# cor = (255, 0, 0)
# cor_circulo = (0, 0, 255)
# cor_linha = (255, 255, 0)
# tela = pygame.display.set_mode((largura, altura)) # set_mode vai receber uma tupla com a largura e a altura da tela
#
# # alterando o nome da janela
# pygame.display.set_caption('Meu Jogo')
#
# # criando o looping (infinito) principal do jogo
# while True:
#     # criando um looping para verificar cada interação do looping principal
#     for event in pygame.event.get():
#         # caso o usuario clique em fechar
#         if event.type == QUIT:
#             pygame.quit()
#             exit()



# VÍDEO 02 - Desenhando objetos
#     # RETÂGUNLO
#     x = 200
#     y = 300
#     comprimento = 40
#     altura = 50
#     pygame.draw.rect(tela, cor, (x, y, comprimento, altura))
#     # CIRCULO
#     x = 300
#     y = 260
#     raio = 40
#     pygame.draw.circle(tela, cor_circulo, (x, y), raio) # a posição x e y do circulo será referênciada no meio dele
#     # LINHA
#     x_1 = 390
#     y_1 = 0
#     x_2 = 390
#     y_2 = 600
#     ponto_1 = (x_1, y_1)
#     ponto_2 = (x_2, y_2)
#     espessura = 5
#     pygame.draw.line(tela, cor_linha, ponto_1, ponto_2, espessura)



# VÍDEO 03 - Movendo objetos
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# largura = 640
# altura_tela = 480
# cor = (255, 0, 0)
# comprimento_retangulo = 40
# altura_retangulo = 50
#
# # colocando o objeto no meio da tela
# meio = (largura/2) - (comprimento_retangulo/2)
# y = 0
# tela = pygame.display.set_mode((largura, altura_tela))
# pygame.display.set_caption('Meu Jogo')
#
# # mudando a velocidade com que o objeto se move na tela atraves do controle da taxa de frames do jogo
# relogio = pygame.time.Clock()
# # OBS.: da para mudar a velocidade alterando o eixo y do obj
#
# while True:
#     relogio.tick(30) # aqui colocamos quantos frames por segundo queremos que nosso jogo tenha
#     # OBS.: qnt maior o número de frames, mais rápido ele vai rodar
#     tela.fill((0, 0, 0)) # a cada iteração a tela é preenchida de preto
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#     pygame.draw.rect(tela, cor, (meio, y, comprimento_retangulo, altura_retangulo))
#
#     # fazendo a lógica para que o retângulo quando chegar ao fim da tela, volte lá em cima
#     if y >= altura_tela:
#         y = 0
#     y += 1
#     pygame.display.update()



# # VÍDEO 04 - Controlando Objeto
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# largura = 640
# altura_tela = 480
# cor = (255, 0, 0)
# comprimento_retangulo = 40
# altura_retangulo = 50
#
# x = (largura/2) - (comprimento_retangulo/2)
# y = (altura_tela/2) - (altura_retangulo/2)
# tela = pygame.display.set_mode((largura, altura_tela))
# pygame.display.set_caption('Meu Jogo')
# relogio = pygame.time.Clock()
#
# while True:
#     relogio.tick(30)
#     tela.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         '''
#         if event.type == KEYDOWN:
#             if event.key == K_a:  # se a tecla pressionada for igual a tecla "a" do teclado acontece algo
#                 x = x - 20  # esquerda
#             if event.key == K_d:
#                 x = x + 20  # direita
#             if event.key == K_s:
#                 y = y + 20  # baixo
#             if event.key == K_w:
#                 y = y - 20  # cima
#         '''
#         if pygame.key.get_pressed()[K_a]:  # se eu pressionar e segura a tecla "a" faça algo
#             x = x - 20  # esquerda
#         if pygame.key.get_pressed()[K_d]:
#             x = x + 20  # direita
#         if pygame.key.get_pressed()[K_w]:
#             y = y - 20  # cima
#         if pygame.key.get_pressed()[K_s]:
#             y = y + 20  # baixo
#     pygame.draw.rect(tela, cor, (x, y, comprimento_retangulo, altura_retangulo))
#     pygame.display.update()



# # VÍDEO 05 - Colissões
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
# x_azul = randint(40, 600)  # se colocassemos (0, 640) poderiamos não ver o retangulo, por isso já estamos
# # desconsiderando seu comprimento
# y_azul = randint(50, 430)  # se colocassemos (0, 480) poderiamos não ver o retangulo, por isso já estamos
# # desconsiderando sua altura
#
# while True:
#     relogio.tick(30)
#     tela.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if pygame.key.get_pressed()[K_a]:  # se eu pressionar e segura a tecla "a" faça algo
#             x -= 20  # esquerda
#         if pygame.key.get_pressed()[K_d]:
#             x += 20  # direita
#         if pygame.key.get_pressed()[K_w]:
#             y -= 20  # cima
#         if pygame.key.get_pressed()[K_s]:
#             y += 20  # baixo
#     ret_vermelho = pygame.draw.rect(tela, cor_vermelho, (x, y, comprimento_retangulo, altura_retangulo))
#
#     # desenhando o retângulo azul
#     ret_azul = pygame.draw.rect(tela, cor_azul, (x_azul, y_azul, comprimento_retangulo, altura_retangulo))
#
#     # condição da colisão
#     if ret_vermelho.colliderect(ret_azul):
#         x_azul = randint(40, 600)
#         y_azul = randint(50, 430)
#     pygame.display.update()