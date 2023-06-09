from functions import *
import time

# Definir as dimensões dos quadradinhos
tamanho_quadradinho = 50

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    
    # Obter o tempo inicial
    tempo_inicial = time.time()
    #print (tempo_inicial)
    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Preencher a tela com a cor preta
    tela.fill(background_color)
    
    ##straight_speed()
    update_ball_position(0.05)
    draw_paddles_a()
    draw_paddles_b()
    move_paddles_a()
    move_paddles_b()
    draw_line_division()
    draw_score()



    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
