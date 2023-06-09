#pong.py

from functions import *
import time

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    # Obter o tempo inicial
    tempo_inicial = time.time()
    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Preencher a tela com a cor preta
    tela.fill(background_color)
    
    # Chamadas de funções
    update_ball_position(0.05)
    draw_racket_a()
    draw_racket_b()
    move_racket_a()
    move_racket_b()
    draw_line_division()
    draw_score()

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
