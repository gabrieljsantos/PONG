from math import *
from setup_tela import *
raio = 12  # Raio da bola

paddles_size_x = 10  # Largura da raquete
paddles_size_y = 50  # Altura da raquete
paddles_color_a = (255, 255, 255)  # Cor da raquete A
paddles_color_b = (255, 255, 255)  # Cor da raquete B
paddles_pos_a_x = 0  # Posição x da raquete A
paddles_pos_a_y = size_tela_y / 2  # Posição y inicial da raquete A
paddles_pos_b_x = size_tela_x - paddles_size_x  # Posição x da raquete B
paddles_pos_b_y = size_tela_y / 2 + paddles_size_y / 2  # Posição y inicial da raquete B
paddles_vel_b = 0  # Velocidade atual da raquete B
paddles_vel_a = 0  # Velocidade atual da raquete A
paddles_acel_a = 0.01  # Aceleração da raquete A
paddles_acel_b = 0.01  # Aceleração da raquete B
paddles_vel_max_a = 6  # Velocidade máxima da raquete A
paddles_vel_max_b = 6  # Velocidade máxima da raquete B

size_line_division_x = 7  # Largura das linhas de divisão
n_dotted = 20  # Número de pontos nas linhas de divisão
spacing = 4  # Espaçamento entre os pontos nas linhas de divisão
color_line_division = (255, 255, 255)  # Cor das linhas de divisão

score_a = 0  # Pontuação do jogador A
score_b = 0  # Pontuação do jogador B
score_value_color = (255, 255, 255)  # Cor do valor da pontuação
ball_color = (255, 255, 255)  # Cor da bola
ball_pos_x = raio + 1 + paddles_size_x  # Posição x inicial da bola
ball_pos_y = raio + 1 + paddles_size_y  # Posição y inicial da bola

ball_speed_x = 15  # Velocidade da bola no eixo x (pixels/s)
ball_speed_y = 23  # Velocidade da bola no eixo y (pixels/s)

decay_rate = 0.1  # Taxa de decaimento da velocidade da raquete

ball_speed_start = [
    (24 + 3*sqrt(2), 14),
    (24 + 3*sqrt(2), -14),
    (-19, -6*sqrt(3)),
    (-19, 6*sqrt(3)),
    (27,0)
]
##(2 + 2*sqrt(2), 27),(2 + 2*sqrt(2), -27),