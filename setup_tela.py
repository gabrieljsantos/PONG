import pygame

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
size_tela_x = 720
size_tela_y = 576

# Criar a tela
tela = pygame.display.set_mode((size_tela_x, size_tela_y))

pygame.display.set_caption("PONG")

# Definir as cores
preto = (0, 0, 0)
branco = (255, 255, 25)